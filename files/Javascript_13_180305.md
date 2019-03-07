# Lesson Javascript_13 (180305[Mon])

## JavaScript Fundamental 13

### Node JS

2. Frontend의 Main Frame Work

   - 상태변화의 감지
   - Ajax를 통해 Request 를 요청하여 Response의 결과값을 받아 DOM제어하여 View를 변화시킨다.
   - 변화감지 : 상태변화를 자동감지하여 View에 영향을 주는 Tool을 이용하여 Angular와 같은 Framework를 접목시켜 작업수행 
   - 일련의 과정 Event - DOM - AJAX

2. Backend의 Main frame Work

   - 정적파일의 제공(HTML파일)
   - REST API(중간에 Data를 Json으로 파싱)
   - DB설계(설계 및 운영)
   - dot net, Jsp, Python, Asp, Java, PHP
   - 대표적 Framework : Spring(Java기반), Django(Python기반)

3. Node.Js

   - Node.Js는 독자적인 모듈시스템을 가지고 있다. require 사용
   - node의 import영역은 동기방식
   - amd는 비동기 

   ```js
   const http = require('http'); // 1 (built-in-model)

   http.createServer((request, response) => { // 2
     response.statusCode = 200;
     response.setHeader('Content-Type', 'text/plain');
     response.end('Hello World');
   }).listen(3000); // 3

   console.log('Server running at http://127.0.0.1:3000/');
   ```

   1. require을 통해 'http'객체를 http에 담는다.(import와 같은 방식)
   2. createSever라는 메서드로 서버에 필요한 모든 프로퍼티들을 만들어낸다.
   3. port번호를 적어주고 localHost로 접속이 가능해진다.

   *npm i -g nodemon 으로 전역으로 nodemon을 설치하면 watch모드를 활용하여 서버를 재기동하지 않아도 실시간으로 바뀐내용을 적용해준다. 실행 할 때엔 nodemon (파일명)으로 실행한다.

   ()  : Parentheses , round bracket (괄호)

   {} : curly bracket (중괄호)

   [] : bracket (대괄호)

### NPM

1. 모듈화
   - javascript는 타언어와는 다르게 모듈기능이 없고 다양한 js파일을 하나로 뭉쳐서 처리하게 된다. javascript특성상 {}단위 변수처리가 일어나지 않기 때문에, 타 js파일과 변수명이 겹치거나 side effect가 일어날 가능성이 높다. 프로젝트가 커지고 다양한 사람들이 협업으로 프로젝트를 진행 할 경우, 데이터를 모듈화하여 합리적으로 사용하는 일은 선택이 아닌 필수 적인 사항인 것이다. 이를 해결하기위해 javascript를 client-side에 국한 시키지 않고 범용적으로 이용하고자하는 움직임이 생겼다. 이때 제안된 것이 CommonJs와 AMD(Asynchronous Module Definition)이다.
2. NPM 이란?
   - NPM(Node Package Manager)은 node.js에서 사용 할 수 있는 모든 모듈들을 패키지화하여 모아둔 repository이다. 여기서 버전관리와 설치까지 도맡아 해주는 매우 유용한 프로그램이다.



### Express

> Express는 Node.js 환경에서 동작하는 Web Application Framework이다.  Web Application 구성에 필요한 Routing, View Helper, Session(영속적 Session관리를 위해서는 Redis등의 Data store가 필요하다)등의 기능을 제공한다.

1. Routing

   - 간단한 AJAX 서버통신

   ```js
   // client-side ajax request
   document.querySelector('button').addEventListener('click', function () {
     const xhr = new XMLHttpRequest();
     xhr.open('POST', '/signin');

     const username = document.querySelector('input[name=username]').value;
     const password = document.querySelector('input[name=password]').value;

     const payload = { username, password };

     xhr.setRequestHeader('Content-type', 'application/json');
     xhr.send(JSON.stringify(payload));

     xhr.onreadystatechange = function () {
       if (xhr.readyState === XMLHttpRequest.DONE) {
         if (xhr.status === 200) {
           console.log(xhr.response)
           document.querySelector('.result').innerHTML = xhr.response;
         } else {
           console.log("Error!");
         }
       }
     };
   });
   ```

   - Route의 정의법

     ![define route](http://poiemaweb.com/img/define-route.png)

     ​





