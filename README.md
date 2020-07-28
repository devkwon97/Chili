### 고추 가격 예측AI

### 참고 자료
* [25년간 고추 가격 데이터](https://www.kamis.or.kr/customer/price/retail/period.do) : 국내 연도별 고추가격 분석 자료<br>
* [25년간 기상청 전국 온도 및 강수량 데이터](https://data.kma.go.kr/climate/StatisticsDivision/selectStatisticsDivision.do?pgmNo=158) : 기상청 정보의 토대로 고추 가격에 영향을 미치는 요인 분석

### 알고리즘
```
텐서플로우를 이용한 다중 선형회귀법으로 AI에게 25년간의 고추 가격과 기상 온도 데이터를 엑셀표에 담아 변인을
입력시켜 변화 되는 과정을 학습 시켜 오차범위를 점차 줄여나가고 클라이언트가 임의의 변인 수를 입력한다면
이미 저장된 학습 모델로 고추 가격을 예측해줌

### 1. 1996년 ~ 2020년 월 단위 평균온도, 최저온도, 최고온도, 강수량, 고추가격
![1](https://user-images.githubusercontent.com/60598284/88687345-1ee3bc00-d133-11ea-8adf-ad0616f26554.PNG)
![2](https://user-images.githubusercontent.com/60598284/88687367-24d99d00-d133-11ea-804d-651263febdf6.PNG)

### 2. 엑셀 지표를 바탕으로 한 고추가격 자동 학습
![3](https://user-images.githubusercontent.com/60598284/88687393-2a36e780-d133-11ea-953d-ab884a24cb0f.PNG)

### 3. 월 단위로 학습 된 고추가격을 4개의 변인 값 온도 강수량 입력시 가격을 예측해줌
![4](https://user-images.githubusercontent.com/60598284/88687400-2c00ab00-d133-11ea-8bd1-899b04b0d7e1.PNG)
