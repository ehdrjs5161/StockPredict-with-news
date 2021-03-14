<<<<<<< HEAD
# 프로젝트 개요 (Overview)
뉴스 데이터를 기반으로 하여 KOSPI 200 주식 종목의 종가를 예측하는 웹 서비스 입니다.

# 프레임 워크 & 라이브러리 (Frame Work & Library)

* Beautiful-Soup

* pykrx

* TensorFlow

* Flask

* React.js

# 데이터 (Data)

* Beautiful-Soup를 이용하여 수집한 2012년 1월 1일 이후 뉴스의 헤드라인 데이터
  
* pykrx를 이용하여 수집한 2012년 1월 1일 이후 KOSPI 200 종목의 주식데이터
  
# 자연어 처리(Natural Language Processing)

* 창원대학교 적응지능연구실(AIR)에서 제공한 긍/부정 감성사전을 이용하여 뉴스의 헤드라인을 긍정, 중립, 부정으로 분류

* 감성분석 결과 값은 하루동안 작성된 뉴스들의 값에 대한 평균으로 주식 데이터와 동기화 작업 진행 후 사용
  
# 딥러닝 (Deep Learning)
 
* 딥러닝의 Features 선정 방법: 상관계수, VIF(Variance Inflation Factor) 사용

* 케라스를 이용한 LSTM 기반으로 이전 28일의 종가, 거래량, 뉴스 감성분석 값을 Features로 하여 다음 개장일, 향 후 7일동안의 종가를 예측

# 웹 (Web)

* python 기반의 코드 실행을 위해 Flask로 서버 구축

* React.js를 이용하여 UI 제공
=======
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
>>>>>>> c240ee6 (Initialize project using Create React App)
