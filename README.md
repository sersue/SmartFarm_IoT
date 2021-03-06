# SmartFarm_IoT 🍄+💻

R&D 사업 - SW융합연구개발과제 연구수행
과제명: IoT 컨테이너 버섯 재배 시설  
활동기간 : 2020.10.19.~2020.4.18  
소요 비용 : 10,000,000원


## 추진 배경 

- 기후에 영향을 많이 받는 농사를 IoT 시설로 옮겨 외부 환경요인에 영향을 덜 받는 환경 조성이 필요하다.  
- 버섯은 수요에 비해 ICT 관련 사업이 많이 활성화 되어있지 않다.  
- 버섯은 환경에 민감해서 완벽한 환경 제어가 필요하다.  
- 농사를 하시는 분 중 나이가 많거나, 몸이 불편하신 분들도 스마트폰 어플로 쉽게 생장 환경을 제어할 수 있게 한다.   

## 시연 영상


## 수행 현황
|수행주차||  
|------|---|  
|1주차|주변 기기 제어를 위한 IoT 학습, 버섯재배의 전반적인 재배과정 이해 /버섯 생장에 필요한 요인 측정을 위한 센서 학습, 최적의 버섯 생장환경 구축을 위한 주변 기기 자료 수집 |
|2주차|서버 구축을 위한 Flask 학습/센서들을 이용한 간단한 센싱 프로그래밍 진행, 타 스마트팜과 연구소 견학을 통해 버섯과 시설 관련 정보 수집 및 자문, 라즈베리파이 <-> 아두이노 무선통신 학습, 컨테이너 내부 배치도 및 전기 설비 구체화 |
|3주차|컨테이너 확보, 배치/컨테이너 단열성능 확인, 내부배치 품목 구입/컨테이너 내부 단열 시공,관리 어플리케이션 제작, 목이버섯 실험배지 확보 /컨테이너 전기설비 설치/실험을 위한 환경요인 상수화 | 
|4주차| 중간보고 발표| 


## 주요 기능 ✨
- (센서) 버섯 생장에 영향을 미치는 환경요인인 이산화탄소, 온도, 습도, 조도를 각각 CO2, 온습도, 조도 센서로 데이터를 입력받는다. 입력받은 데이터를 클라우드 서버에 10초를 주기로 업데이트 하여 실험의 최종 목표인 환경요인에 따른 버섯의 생장 정도를 수치화 및 분석 할 수 있다.

 - (센서*제어장비 연동) 센서에 입력되는 값이 이상적인 값보다 높거나 낮을 때 이산화탄소 농도는 외부와 연결된 팬, 온도는 라디에이터, 습도는 가습기를 작동시켜 환경을 각각 제어할 수 있는 시스템을 설비할 수 있다. 이를 통해 버섯 생장에 미치는 외부 환경적인 요인을 최소화할 수 있다. 
 
- 컨테이너를 아두이노로 설비하여 다른 스마트팜 보다 비교적 저렴한 가격으로 IoT 시설을 조성할 수 있다. 

## Screenshot
![KakaoTalk_Photo_2021-01-21-23-26-05](https://user-images.githubusercontent.com/42709887/105365001-26e36b00-5c41-11eb-9eda-e00020486e19.jpeg)
![KakaoTalk_Photo_2021-01-21-23-26-23](https://user-images.githubusercontent.com/42709887/105365008-2945c500-5c41-11eb-901d-e10b38979a1e.jpeg)

## Requirements

- Database는 읽기용 로컬 Mysql, 읽기(Every 1s),쓰기용(Every 10s) 클라우드 Firbase 로 나누어서 저장된다. 
- 서버 : 라즈베리파이에 서버를 올려서 사용한다.
- 아두이노: 센서는 총 3가지를 사용하며(이산화탄소, 온습도, 조도) 와이파이를 사용하기 위해 esp8266 모듈을 사용한다.
- 제어 어플리케이션 : flutter

## 제어 흐름도 (scenario)

1. 제어 어플리케이션 (Flutter)를 사용하여 Auto mode, 직접 제어 mode를 선택할 수 있다.  
1.1  Auto mode를 사용하면 센서 값을 지정값으로 자동 제어 해준다.  
1.2 직접 제어 mode를 통해 릴레이로 전기를 제어할 수 있다.  

## Role
|이름 |Main Role|  
|------|---|  
|문수림|시설 설비, 아두이노 설치 및 서버 DB개발|
|고동현|시설 설비, 아두이노 설치 및 서버 DB개발|
|왕종휘|시설 설비, 아두이노 설치 및 서버 DB개발|
