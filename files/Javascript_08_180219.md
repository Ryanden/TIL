# Lesson Javascript_08 (180219[Mon])

## JavaScript Fundamental 08

### DOM(Document object model)

- 이벤트 처리를 위한 이벤트 핸들러를 만듦
- DOM을 사용할경우 html에 java script가 종속된다.
- html이 자꾸 변경되게 되어 유지보수에 문제가 발생한다
- Document(html)은 html, CSS, java script 모두를 포함한다. (메서드)
- 브라우저가 html을 읽고 파싱하여 각 data를 object로 만들어 저장한다.
- DB에서 JSON형태로 문자열 파일을 가져오는데 정보를 객체화 하여 브라우저로 가져온다.
- DB에서는 정보를 파일형태로, JSON은 문자열로, 브라우저에서는 객체형태로 가지고 있다.
- model은 data와 관련이 있다. 

### Dom내부의 노드

- 브라우저는 HTML을 로드하고 파싱하고 DOM tree를 만든다.   

![DOM tree](http://poiemaweb.com/img/dom-tree.png)

- JS가 접근할때 진입점 document를 통해 접근하여 각 요소를 조작한다.
- 모든 요소의 종점은 text노드이다. 모든 요소는 text노드를 갖는다.
- 모든 li의 객체를 전달 받을때 유사배열객체 형태로 받아온다.

### Dom Query / Traversing  (요소선택 / 탐색)

1. document.getElementbyID(id)

   - ID로 선택

2. document.getElementClassName(class)

   - length 프로퍼티가 있는건 반복자 가능
   - collection(live)를 반환한다.

   ```js
   // HTMLCollection을 반환한다.
   var elems = document.getElementsByClassName('red');

   for (var i = 0; i < elems.length; i++) {
     // 클래스 어트리뷰트의 값을 변경한다.
     elems[i].className = 'blue';
   }
   ```

   - 위 코드의 경우 두번째만 red가 blue로 바뀐다. live의 경우 collection 내부의 length가 실시간으로 변경되어 0번과 2번 인덱스에 접근하지 못하고 종료된다. 

3. 요소마다 독특하게 지니는 정보들을 각 엘리먼트 요소가 가지고 있다.

## 비동기 / 동기

### 이벤트 루프

```js
function func1() {
  console.log('func1');
  func2();
}

function func2() {
  setTimeout(function() {
    console.log('func2');
  }, 0);

  func3();
}

function func3() {
  console.log('func3');
}

func1();
```

![event-loop](http://poiemaweb.com/img/event-loop.gif)

루프 동작 원리

### Event Flow(이벤트의 흐름)

![event flow](http://poiemaweb.com/img/eventflow.svg)

- 캡쳐링과 버블링으로 이벤트를 제어 할 수 있다.

