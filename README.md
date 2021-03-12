# 프로젝트 개요 (Overview)
뉴스 데이터를 기반으로 하여 KOSPI 200 주식 종목의 종가를 예측하는 웹 서비스 입니다.

# 프레임 워크 & 라이브러리 (Frame Work & Library)

* Beautiful-Soup

* pykrx

* TensorFlow

* Flask

* React.js

# 데이터 (Data)

  * Beautiful-Soup를 이용하여 수집한 2012년 1월 1일 이후 뉴스 데이터
  
  * pykrx를 이용하여 수집한 2012년 1월 1일 이후 KOSPI200의 주식데이터
  
# 자연어 처리(Natural Language Processing)

* 창원대학교 적응지능연구실(AIR)에서 제공한 긍/부정 감성사전을 이용하여 뉴스의 헤드라인을 긍정, 중립, 부정으로 분류

  
# 딥러닝 모델 (Deep Learning Model)
 
* 딥러닝 모델 Features 선정 방법: 상관계수, VIF(Variance Inflation Factor) 사용

* TensorFlow의 케라스를 이용한 LSTM 기반으로 이전 28일의 종가, 거래량, 뉴스 감성분석 값을 Features로 하여 다음 날의 종가를 예측


