# Lesson Javascript_05 (180205[Mon])

## JavaScript Fundamental 05

### 1. Javascript Built-in Object

- 내장 객체에는 많은 프로그래머들이 사전에 많이 사용되는 기능들을 표준화시켜 사용의 편의를 도모하였다. (API) OS가 하드웨어를 제어한다. 

> 메소드의 작동원리

> 메소드 \> 자바스크립트 \> 브라우저 \> OS \> 드라이버 \> 하드웨어



- 브라우져기능 (뒤로가기,새로고침,사이트이동 등등) BOM


- 윈도우 객체 하나를 모두가 사용하며, window 객체 안에는 수많은 프로퍼티들이 내장 되어있다.

```js
window.String();
window.Number();
```

- 객체를 생성할 필요가 없는 메소드를 static 메소드라 한다.
- Number.isNaN()과 같은 객체생성없이 static으로 호출가능한 프로퍼티들이 있다.



### 2. Javascript Standard Built-in Objects(표준 빌트인 객체)

#### 1. 전역함수

##### 1.1 eval()

- eval() 함수는 사용하지 않는 것이 좋다. 사용자로 부터 입력받은 컨텐츠를 eval() 안에 넣으면 자바스크립트는 실행해버리므로 보안에 취약하니 주의를 요한다.

  ```js
  var foo = eval('2 + 2');
  var x = 5,
      y = 4;
  console.log(foo); // 4
  console.log(eval('x * y')); // 20
  ```

  ​

##### 1.2 isFinite()

- 매개변수에 전달된 값이 유한수인지 검사하여 그 결과를 Boolean 으로 반환하나, 매개변수가 숫자가 아닐 경우, 숫자로 변환하여 검사를 수행한다.

  ```js
  console.log(isFinite(Infinity));  // false
  console.log(isFinite(NaN));       // false
  console.log(isFinite('Hello'));   // false
  console.log(isFinite('2005/12/12'));   // false

  console.log(isFinite(0));         // true
  console.log(isFinite(2e64));      // true
  console.log(isFinite(null));      // true: null->0
  ```

##### 1.3 isNaN()

- 매개변수의 전달된 값이 NaN(Not a Number)일경우를 검사하여 그 결과를 Boolean으로 반환하며, 매개변수가 숫자가 아닐 겨우, 숫자로 변환한후 검사를 수행한다.

  ```js
  isNaN(NaN)       // true
  isNaN(undefined) // true: undefined -> NaN
  isNaN({})        // true: {} -> NaN
  isNaN('blabla')  // true: 'blabla' -> NaN

  isNaN(true)      // false: true -> 1
  isNaN(null)      // false: null -> 0
  isNaN(37)        // false

  // strings
  isNaN('37')      // false: '37' -> 37
  isNaN('37.37')   // false: '37.37' -> 37.37
  isNaN('')        // false: '' -> 0
  isNaN(' ')       // false: ' ' -> 0

  // dates
  isNaN(new Date())             // false: new Date() -> Number
  isNaN(new Date().toString())  // true:  String -> NaN
  ```

##### 1.4 parseInt()

- 매개변수에 전달된 문자열을 정수형 숫자로 변환하여 반환한다.

##### 1.5 encodeURI() / decodeURI()

- encodeURI()은 매개변수로 전달된 URI(Uniform Resource Identifier)를 인코딩한다.

  ![uri](http://poiemaweb.com/img/uri.png)

```js
var uri = 'http://example.com?name=홍길동&job=programmer&teacher';
var enc = encodeURI(uri);
var dec = decodeURI(enc);
console.log(enc);
// http://example.com?name=%EC%9D%B4%EC%9B%85%EB%AA%A8&job=programmer&teacher
console.log(dec);
// http://example.com?name=홍길동&job=programmer&teacher
```

- 부동소수점(floating point number)

  \# Fragment(조각) 뒤로 나오는건 서버가 받지 않는다.

  컴포넌트(scheme, host, part ,path query parameter) 구성요소



### 새로 알게 된 점들

- 문자열은 Immutable 한 특성을 지니고 있으나 특별한 상황 즉, str.length와 같은 객체화를 실행하려고 하면문자열은 객체화가 되어 String()의 내부 프로퍼티에 접근하여 객체처럼 사용되는데 이를 wrapping이라고 한다. 
- 비동기함수는 try catch로 에러 캐치가 안되므로 사용상 주의가 필요하다.
- string은 유사배열객체이다. 이 특성을 이용하여 string을 배열처럼 사용 할 수 있다.
- 배열은 순회가 가능하다. for문처럼 사용이 가능하다는 말이다.

