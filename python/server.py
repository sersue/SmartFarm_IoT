import time
import datetime
import websockets
import asyncio
import threading
# import Adafruit_DHT as dht₩
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
import json
# import RPi.GPIO as GPIO 




cred = credentials.Certificate("funani-farm-firebase-adminsdk-krr41-07f5497e8c.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

lock = threading.Lock()

recv_msg = ""
connected = set()
flag_sensor = False
flag_localWriter = False

deviceStatus = {
    "autoControll" : False,
    "airTemp" : 20,
    "airHumidity" : 50,
    "led" : False,
    "airCondition" : False,
    "ph" : 6.5,
    "humidifier" : False,
    "waterTemp" : 20,
    "waterPump" : False,
    "innerFan" : False,
    "outerFan" : False,
    "heater" : False,
    "ec" : 1.01,
    "co2" : 0,
    "lux" : 0
}

autoPilotMode = {
    "humidifierON" : 80,
    "humidifierOFF" : 99,
    "heaterON" : 10,
    "heaterOFF" : 20,
    "outerFanON" : 800,
    "outerFanOFF" : 500,
}

def pushFirestore():
    print(u'===========PUSHING============')
    now = datetime.datetime.now()
    now_dict = {"timestamp" : now}
    now_dict.update(deviceStatus)
    now_dict.update(autoPilotMode)
    db.collection("report").document(str(now)).set(
        now_dict
    )
    print(u'=={}=='.format(str(datetime.datetime.now())))
    print(u'==============================')

def jobDone(doc):
    print(u'\n\n=============DONE=============')
    doc.document.reference.update({
        'isFinished' : True
    })
    print(u'=={}=='.format(str(datetime.datetime.now())))
    print(u'==============================')

class LocalWriter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
            
    def run(self):
        global flag_localWriter, deviceStatus
        while True:
            if((flag_localWriter != flag_sensor)& (len(recv_msg)>10)) :
                with lock:
                    print("!!!!!!!!!!!!!lock!!!!!!!!!!!!!")
                    
                    result = json.loads(recv_msg)
                    deviceStatus['airTemp']= result['airTemp']
                    deviceStatus['airHumidity']= result['airHumidity']

                    print("deviceStatus : "+str(deviceStatus['airTemp']))
                    print("deviceStatus : "+str(deviceStatus['airHumidity']))
                    flag_localWriter = flag_sensor
                    print("############unlock############")
            

class FirebaseWriter (threading.Thread):
    def __init__ (self):
        with lock:
            threading.Thread.__init__(self)
            print("======initializing start======")
            print("!!!!!!!!!!!!!lock!!!!!!!!!!!!!")
            temp = db.collection('report').order_by(u'timestamp',direction= firestore.Query.DESCENDING).limit(1).get()[0]
            temp_map = temp.to_dict()
            print("LATEST LOG AT : "+temp.id)
            print("LATEST LOG DATA :  "+str(temp_map))
            deviceStatus.update({
                "autoControll" : temp_map['autoControll'],
                "airTemp" : temp_map['airTemp'],
                "airHumidity" : temp_map['airHumidity'],
                "led" : temp_map['led'],
                "airCondition" : temp_map['airCondition'],
                "ph" : temp_map['ph'],
                "humidifier" : temp_map['humidifier'],
                "waterTemp" : temp_map['waterTemp'],
                "waterPump" : temp_map['waterPump'],
                "innerFan" : temp_map['innerFan'],
                "outerFan" : temp_map['outerFan'],
                "heater" : temp_map['heater'],
                "ec" : temp_map['ec'],
                "co2" : temp_map['co2'],
                "lux" : temp_map['lux']
            })

            autoPilotMode.update({
                "humidifierON" : temp_map['humidifierON'],
                "humidifierOFF" : temp_map['humidifierOFF'],
                "heaterON" : temp_map['heaterON'],
                "heaterOFF" : temp_map['heaterOFF'],
                "outerFanON" : temp_map['outerFanON'],
                "outerFanOFF" : temp_map['outerFanOFF'],
            })
            print("############unlock############")
            print("====initializing finished=====\n\n")
            

    def run(self):
        while True:
            with lock:
                print("!!!!!!!!!!!!!lock!!!!!!!!!!!!!")
                pushFirestore()
                print("############unlock############\n\n")
            time.sleep(10)

class FirebaseReader (threading.Thread):
    def on_snapshot(self,col_snapshot, changes, read_time):
        for doc in changes:
            if doc.type.name == 'ADDED':
                with lock:
                    print("!!!!!!!!!!!!!lock!!!!!!!!!!!!!")
                    print(u'=====New Request Received=====')
                    print(u'=={}=='.format(doc.document.id))
                    print(u'==============================\n\n')
                    if doc.document.get('dataType') == "control":
                        deviceStatus[doc.document.get('target')] = doc.document.get('operation')
                        pushFirestore()
                        jobDone(doc)
                    elif doc.document.get('dataType') == "autoPilotChange":
                        autoPilotMode.update(doc.document.get('value'))
                        pushFirestore()
                        jobDone(doc)
                    print("############unlock############\n\n")

    order_query = db.collection('order').where(u'isFinished', u'==', False)

    def run(self):
        self.order_query.on_snapshot(self.on_snapshot)
        while True:
            time.sleep(1)

async def handler(websocket, path):
    global flag_sensor,recv_msg
    connected.add(websocket)
    print("{0}번째 : {1} 연결".format(len(connected),websocket))
    try:
        while True :
            recv_msg = await websocket.recv()
            if(flag_sensor):
                flag_sensor = False
            else :
                flag_sensor = True
            
            print(recv_msg)
    
    except websockets.exceptions.ConnectionClosed:
        connected.remove(websocket)
        print("비정상적으로 연결 종료")
    finally:
        if websocket in connected : 
            connected.remove(websocket)
            print("정상적으로 연결 종료")
    

if __name__ == '__main__' :
    # dht22 = Sensor_DHT22()
    firebaseWriter = FirebaseWriter()
    firebaseReader = FirebaseReader()
    localWriter = LocalWriter()

    firebaseWriter.start()
    firebaseReader.start()
    localWriter.start()
    
    try:
        ws_server = websockets.serve(handler,"", 5000)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(ws_server)
        loop.run_forever()

    except KeyboardInterrupt:
        print("비정상 종료")
    
    finally :
        print("종료")