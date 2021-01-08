import serial

PORT = '/dev/cu.usbserial-1430'
BaudRate = 9600

ARD=serial.Serial(PORT,BaudRate)

def Decode(A):
    A = A.decode()
    A = str(A)
    if A[0] == 'C':
        if (len(A)==6):
            Ard1 = int(A[1:4])
            result = Ard1
            return result 
        else :
            print("Error_lack of number _ %d" %len(A))
            return False      
    else :
        print("Error_Wrong Signal")
        return False

def Ardread():
    if ARD.readable():
        LINE = ARD.readline()
        code = Decode(LINE)
        print(code)
        return code
    else : 
        print("fail")

while True:
    Ardread()