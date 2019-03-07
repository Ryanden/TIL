# Lesson Javascript_11 (180223[Fri])

## JavaScript Fundamental 11

### AJAX (Asynchronous Java Script and XML)

```js
var xhr = new XHLHTTPRequest();
//
xhr.open('GET','/todos')  // ('', '/URL',비동기처리여부 = true) get은 바디가 비어져 있다. url을 넘겨준다. 데이터가 없을 수 있다.
// post의 경우 데이터가 항상 들어있다. 즉 payload가 있다. payload를 가지고 데이터를 갱신한다. 
// get인데 parameter가 없으면 전부 요청하는것
// XMLHttpRequest.setRequestHeader로 header를 설정가능
xhr.send()	// payload = request message를 보냄 (body에 내용이 있거나 없기도함)
```

### Ajax 응답 처리의 예

```js
// XMLHttpRequest.readyState 프로퍼티가 변경(이벤트 발생)될 때마다 이벤트 핸들러를 호출한다.
req.onreadystatechange = function (e) {
  // readyStates는 XMLHttpRequest의 상태(state)를 반환
  // readyState: 4 => DONE(서버 응답 완료)
  if (req.readyState === XMLHttpRequest.DONE) {
    // status는 response 상태 코드를 반환 : 200 => 정상 응답
    if(req.status === 200) {
      console.log(req.responseText);
      // 비동기 함수이기때문에 responseText를 외부로 가져갈수없다!
    } else {
      console.log("Error!");
    }
  }
};
```



### REST API

Get은 조회를 의미한다.

column은 idea 즉 허상 껍데기를 의미한다.

row는 그안의 속성들을 의미한다

index : 조회 

retrieve : 검색

GET : payload가 있거나 없을수도 있으며 data를 조회

POST : payload가 있으며 새로운 data를 생성

DELETE : payload가 있으며 선택한 data를 삭제

PUT : payload가 있으며 사용자의 원하는 내용으로 data를 대체