# Lesson Javascript_10 (180222[Thu])

## JavaScript Fundamental 10

### AJAX (Asynchronous Java Script and XML)

- meta data 는 data를 수식해주는 data이다. 즉, 특정 데이터를 더 자세하게 설명해주는 data이다. 

- Ajax 이전의 통신 방식

  ![Request & Response](http://poiemaweb.com/img/req_res.png)

- Client가 HTML파일을 서버에 요청하고 Server는 HTML파일을 전송해주고 Client의 컴퓨터는 전송받은 HTML파일을 토대로 브라우저의 Rendering engine에 HTML, CSS를 로드하고 Parsing하여 DOM tree, CSSOM tree를 만들어 그 정보를 토대로 Rendering한다.

#### 브라우저가 화면을 전환하는 경우

1. 브라우저에 새로운 URI를 전송하여 새로운 정보를 요청한다.
2. 웹페이지의 링크관련 버튼을 눌러서 새로운 URI을 요청한다.
3. 브라우저의 앞으로, 뒤로 버튼을 눌러 history기록의 앞 뒤의 URI을 요청한다.

#### SEO (Search Engine Optimizing)

- Ajax의 SEO문제가 있다. 
- 서버의 연결 기록 방식 cookie - session - token

#### 기존의 통신방식

- 전체 HTML 파일 요청 및 전송
- HTML의 Re rendering으로 인한 화면 깜박임 발생

#### Ajax의 통신방식

- 변경사항이 없는 부분은 재요청하지 않고 변경사항이 발생한 부분의 데이터만 API를 통해 Json형식으로 서버에 요청하고 송신 받아 전체를 다시 rendering 하지 않고 변경사항이 발생한 부분만 다시 rendering 하여 패킷소모도 줄이고, 속도도 높히고 화면의 깜박임 현상도 방지
- Server내에서 HTML을 만들어서 Client에게 전송할 경우 Server Rendering 이라고 하는데 이런 경우에는 SEO 문제를 어느정도 해결해주는데 도움이 된다.

#### JSON (JavaScript Object Notation)

- Client가 Sever에 Data를 요청할때 JS의 데이터 타입으로 텍스트를 요청한다.
- HTTP통신 방식에서는 문자열을 서로 주고 받는다.
- 객체형태의 JS파일을 json타입의 형태로 변환하여 요청하고 Server는 json타입의 형태로 전송하고 브라우저는 그걸 받아서 객체형태로 변환하여 rendering해준다.

#### XML HTTP Request

- XMLHttpRequest 생성자함수의 객체생성

- 비동기방식으로 request

  ```js
  // XMLHttpRequest 객체의 생성
  var xhr = new XMLHttpRequest();
  // 비동기 방식으로 Request를 오픈한다
  xhr.open('GET', '/users');

  // open 통신하기위한 준비 메서드 (Get방식으로 url을 보냄)

  // Request를 전송한다
  xhr.send();
  ```

#### MVC (Model View Controller)

- Client와 Server간의 데이터가 변경되는 사항을 감지하여 양쪽에 동일한 상태를 유지해주는 방식
- MVC - MVVC - MVC* - CBD로 발전 

![HTTP request response message](http://poiemaweb.com/img/HTTP_request+response_message.gif)

get방식

- get방식은 pay로드가 없다.

```js 
req.send(null);
// req.send('string');
// req.send(new Blob()); // 파일 업로드와 같이 바이너리 컨텐트를 보내는 방법
// req.send({ form: 'data' });
// req.send(document);
```

post방식

- post방식은 pay로드가 있다.

content-type : client가 요청하는 데이터 타입

accept : client가 송신받을 데이터타입

status line = 작업후의 메시지 200

Response가 200 = 요청한 html 성공

400 = 접근 불가



