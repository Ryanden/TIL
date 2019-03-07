# Lesson Javascript_07 (180208[Thu])

## JavaScript Fundamental 07

###  Javascript 생성자함수

```js
// 생성자함수로 person 인스턴스를 만들기
function Person(name){
this.name = name,
this.myName = function() {return console.log(this.name);}
}
var person1 = new Person('lee');
person1.myName();
```

### 실행 컨텍스트와 자바스크립트 동작원리

#### 1. 실행 컨텍스트

- **실행 가능한 코드를 형상화하고 구분하는 추상적인 개념**이라고 정의한다. 좀 더 쉽게 말하자면 **실행 컨텍스트는 실행 가능한 코드가 실행되기 위해 필요한 환경**

- 1. 실행의 가능성이 있는 코드들(함수)이 실행되어지려면 환경이 필요하다.

  2. 필요한 정보들을 담는 자료구조들을 만들고 객체화하여 관리한다.

     ```js
     var x = 'xxx';

     function foo () {
       var y = 'yyy';

       function bar () {
         var z = 'zzz';
         console.log(x + y + z);
       }
       bar();
     }
     foo();
     ```

     스택자료구조 형태로 실행컨텐스트들을 가지고 있다.

     ![img](http://poiemaweb.com/img/ec_1.png)

     코드를 실행하기 이전에 전역컨텍스트를 만들고 전역부터 실행해나간다. 함수문을 만나면 그 함수문의 함수 컨텐스트를 만들고 내부함수호출문을 만나면 내부함수의 컨텍스트 객체도 만든다. 내부함수가 종료되면 실행컨텍스트 내부에 가장위에있던 내부함수 컨텍스트 객체를 pop()하여 빼내어 실행컨텍스트 내부에 data를 제거하고 바로 직전 실행 컨텍스트에게 제어권을 넘긴다.

#### 2. 실행컨텍스트의 3가지 객체

![img](http://poiemaweb.com/img/excute_context_structure.png)

VO(Variable object)는 변수,함수선언식, 함수인수들을 관리한다.

SC(Scope Chain)은 스코프들을 관리한다.

TV(This Value)는 this 컨텍스트들을 관리한다.

##### 2.1 Variable Object(VO / 변수객체)

- VO객체는 vars(변수들), function declarations(함수선언식)과 같은 프로퍼티들을 담고 있다.

  - 변수
  - 매개변수, 인수정보
  - 함수 선언(함수 표현시은 제외)

- 전역컨텍스트의 경우

  ![ec-vo-global](http://poiemaweb.com/img/ec-vo-global.png)

  - 전역코드는 명시적으로 호출할 수 없다. 매개변수도 없고 arguments도 없다.
  - 함수코드는 호출도 가능하며 매개변수도 있고 인수(arguments)가 있다.
##### 2.2 Scope chain

  - 스코프체인은 리스트를 갖는다.

    ![ec-sc](http://poiemaweb.com/img/ec-sc.png)

##### 2.3 this value

- 기본적으로 this는 window를 가리키지만 this를 사용할 경우 그 객체의 가리키는 정보를 바꾼다.

#### 3. 실행컨텍스트 생성 과정
##### 3.1 전역 코드에의 진입

##### GO(Global Object)를 생성 (window 즉,built-in Object들이 있는) 

![초기 상태의 실행 컨텍스트](http://poiemaweb.com/img/ec_3.png)

전역 객체가 생성된 이후 전역 코드로 컨트롤이 진입하면 전역 실행 컨텍스트 객체가 생성되고 실행 컨텍스트객체 내부에 stack형태로 쌓인다.

![전역 실행 컨텍스트의 생성](http://poiemaweb.com/img/ec_4.png)

전역객체내부에 있는것은 모두 전역객체의 것

##### 3.2 변수 x의 선언 처리

**var 키워드로 선언된 변수는 선언 단계와 초기화 단계가 한번에 이루어진다.** 다시 말해 스코프 체인이 가리키는 변수 객체에 변수가 등록되고 변수는 undefined로 초기화된다. 따라서 변수 선언문 이전에 변수에 접근하여도 Variable Object에 변수가 존재하기 때문에 에러가 발생하지 않는다. 다만 undefined를 반환한다. 이러한 현상을 **변수 호이스팅(Variable Hoisting)**이라한다.

##### 3.3 this value 결정

변수 선언 처리가 끝나면 다음은 this value가 결정된다. **this value가 결정되기 이전에 this는 전역 객체를 가리키고 있다가 함수 호출 패턴에 의해 this에 할당되는 값이 결정된다.** 전역 코드의 경우, this는 전역 객체를 가리킨다.



## 클로저

### 1. 클로저의 개념

- **클로저는 내부함수가 참조하는 외부함수의 지역변수가 외부함수에 의해 내부함수가 반환된 이후에도 life-cycle이 유지되는 것을 의미한다.**

### 2. 클로저의 활용

```html
<!DOCTYPE html>
<html>
  <body>
  <p>클로저를 사용한 Counting</p>

  <button type="button" onclick="myFunction()">Count!</button>

  <p id="demo">0</p>

  <script>
    var add = (function () {
      var counter = 0;
      return function () {
        return ++counter;
      };
    }());

    function myFunction() {
      document.getElementById('demo').innerHTML = add();
    }
  </script>
  </body>
</html>
```





