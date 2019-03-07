# Lesson Javascript_03 (180201)  
## JavaScript Fundamental 03

### 1. 객체(object)란?

1. 프로퍼티
2. 메소드

### 2. 객체생성방법

1. literal방식

   - 객체를 하나만 단기적으로 사용하는 경우에 사용하면 좋다.

   ```js
   var emptyObject = {};
   console.log(typeof emptyObject); // object

   var person = {
     name: 'Lee',
     gender: 'male',
     sayHello: function () {
       console.log('Hi! My name is ' + this.name);
     }
   };

   console.log(typeof person); // object
   console.log(person); // { name: 'Lee', gender: 'male', sayHello: [Function: sayHello] }

   person.sayHello(); // Hi! My name is Lee
   ```

   ​

2. object생성자함수를 사용

   ```js
   // 빈 객체의 생성
   var person = new Object();
   // 프로퍼티 추가
   person.name = 'Lee';
   person.gender = 'male';
   person.sayHello = function () {
     console.log('Hi! My name is ' + this.name);
   };

   console.log(typeof person); // object
   console.log(person); // { name: 'Lee', gender: 'male', sayHello: [Function] }

   person.sayHello(); // Hi! My name is Lee
   ```

   ​

3. 생성자(constructer)함수

   - 생성자 함수가 객체를 생성하면서 가리킬 포인터를 this로 표기한다.

   ```js
   // 생성자 함수
   function Person(name, gender) {
     this.name = name;
     this.gender = gender;
     this.sayHello = function(){
       console.log('Hi! My name is ' + this.name);
     };
   }

   // 인스턴스의 생성
   var person1 = new Person('Lee', 'male');
   var person2 = new Person('Kim', 'female');

   console.log('person1: ', typeof person1);
   console.log('person2: ', typeof person2);
   console.log('person1: ', person1);
   console.log('person2: ', person2);

   person1.sayHello();
   person2.sayHello();
   ```

   유사배열객체

   ###  3. 객체 프로퍼티의 접근

   1. 프로퍼티이름

   2. 프로퍼티 값

      - 케밥케이스(first-name)를 사용하여 프로퍼티 명을 해줘야 할 경우, 대괄호 []를 사용하여 ['first-name']으로 해주지 않으면 -를 연산자로 판단하여 연사하려 하고 first와 name을 변수로 판단하게 된다.

   3. 프로퍼티 값 갱신
      - 객체가 이미 소유하고 있는 프로퍼티에 새로운 값을 할당하면 값이 갱신된다.

   4. 프로퍼티 동적 생성

   5. 프로퍼티 삭제

      - 삭제가 가능하나 사용 하지 않는다.(처음부터 만들지 않으면 되기때문)

      ```js
      var person = {
        'first-name': 'Ung-mo',
        'last-name': 'Lee',
        gender: 'male',
      };

      delete person.gender;
      console.log(person.gender); // undefined

      delete person;
      console.log(person); // Object {first-name: 'Ung-mo', last-name: 'Lee'}
      ```

   6. for-in문

      ```js
      var person = {
        'first-name': 'Ung-mo',
        'last-name': 'Lee',
        gender: 'male'
      };

      // prop에 객체의 프로퍼티 이름이 반환된다. 단, 순서는 보장되지 않는다.
      for (var prop in person) {
        console.log(prop + ': ' + person[prop]);
      }

      /*
      first-name: Ung-mo
      last-name: Lee
      gender: male
      */

      var array = ['one', 'two'];

      // index에 배열의 경우 인덱스가 반환된다
      for (var index in array) {
        console.log(index + ': ' + array[index]);
      }

      /*
      0: one
      1: two
      */
      ```


### 4. 객체 프로퍼티의 접근

```js
// Pass-by-reference
var foo = {
  val: 10
}

var bar = foo;
console.log(foo.val, bar.val); // 10 10
console.log(foo === bar);      // true

bar.val = 20;
console.log(foo.val, bar.val); // 20 20
console.log(foo === bar);      // true
```

- foo와 bar 각각의 변수는 동일한 주소값을 지닌다. 즉, foo를 변경하면 bar의 내용이 같이 변경된다. 의도하지 않은 부수효과(side effect)가 발생. 부수효과가 발생하지 않도록 만든것이 순수함수.

  [예시]

  ![프로퍼티 접근 예시 그림1](http://poiemaweb.com/img/pass-by-ref.png)

- 변수 foo와 bar는 동일한 값을 공유하고있다. 변수는 주소값을 지니고 있으니 즉, 두개의 주소값이 하나의 값을 가리키고 있는것이다.

  ​

### 5. 객체의 분류

![객체의 분류 그림 1](http://poiemaweb.com/img/object.png)



- 객체를 생성자 함수로 생성해낸 객체는 인스턴스라고 한다.
- Standard Built-in Object는 브라우져와 관계없는 객체
- Host Object : 사용자가 생성한 객체



## 함수

### 1. 함수란?

- 특정 작업을 수행하기위한 일련의 구문들을 그룹화하기 위한 개념이다.

- 구문의 재사용과 효율성을 증대시키며 가독성을 높힌다.

- 함수는 객체이며 일급객체이다. 즉, 다른 값들 처럼 사용이 가능하며, 변수나 객체 배열등에 저장이 가능하다는 특징이 있다.

  1) 함수 선언식(Function declaration)

  ```js
  function square(number) {
    return number * number;
  }
  /* function 함수명 (인자값){
  		식;
  }*/
  ```

  - return을 넣어주지 않을경우 잠정적 (return undefined) 한다.

  2) 함수 표현식(Function expression)

  - 일급객체 4가지 특징

  > 1. 무명의 리터럴로 표현이 가능하다.
  >
  >    ```js
  >    var square = function(number) {
  >      return number * number;
  >    };
  >    // 함수명이 없는 무명함수
  >    // 변수 square는 참조로 function을 가리키고 있다
  >    // 호출할때는 square로 호출한다.
  >    ```
  >
  >    - 이러한 함수를 익명 함수(anonymous function)이라 한다. // 함수표현식에서는 함수명을 생략하는 것이 일반적이다.
  >
  >      ```js
  >      // 기명 함수표현식(named function expression)
  >      var foo = function multiply(a, b) {
  >        return a * b;
  >      };
  >      // 익명 함수표현식(anonymous function expression)
  >      var bar = function(a, b) {
  >        return a * b;
  >      };
  >
  >      console.log(foo(10, 5)); // 50
  >      console.log(multiply(10, 5)); // Uncaught ReferenceError: multiply is not defined
  >      ```
  >
  >      ​
  >
  > 2. 변수나 자료 구조(객체, 배열…)에 저장할 수 있다.
  >
  > 3. 함수의 파라미터로 전달할 수 있다.
  >
  > 4. 반환값(return value)으로 사용할 수 있다.
  >
  >    - 함수자신이 함수를 부를 경우 재귀함수라 한다. 디버깅을 할때 사용하나, overflow나 각종 문제를 야기 할 수 있다.

  3) function() 생성자 함수

  - 다음의 함수는 함수가 내부에서 함수문을 처리하는 방식이다. 

  ```js
  var square = new Function('number', 'return number * number');
  console.log(square(10)); // 100
  ```

### 2. 함수 호이스팅

- 모든 선언문을 스코프의 선두로 옮긴것 처럼 동작하는 현상
- 실행컨텍스트
  - 코드를 실행하기 이전 모든 선언문들을 확인한다. VO(variable object)에 저장한다. 현재는 선언 단계(Declaration phase)이다. 이후로 초기화 단계(Initialization phase)로 넘어가서 변수들을 메모리에 할당한다. 이 단계에서 모든 변수는 undefined로 초기화하여 메모리에 할당한다. 마지막으로 할당 단계(Assignment phase)에 undefined로 초기화된 변수에 실제값을 할당한다.
  - 자바스크립트는 일련의 3단계 에서 2단계까지 실행하므로 변수를 선언하지 않고 사용해도 참조는 가능하다.
  - 함수호이스팅은 변수호이스팅과 다르게 3단계를 한번에 실행한다. 함수 선언식만 가능하다. 
  - 함수를 변수에 담기때문에 변수호이스팅의 법칙을 따른다.
  - 함수선언식으로 함수를 정의하면 사용하기에 쉽지만 대규모 애플리케이션을 개발하는 경우 인터프리터가 너무 많은 코드를 변수 객체(VO)에 저장하므로 애플리케이션의 응답속도는 현저히 떨어질 수 있으므로 주의해야 할 필요가 있다.


### 3. 매개변수(Parameter, 인자)

1.  매개변수(parameter, 인자) vs 인수(argument)

  - 매개변수는 함수 내에서 변수와 동일하게 메모리 공간을 확보하며 함수에 전달한 인수는 매개변수에 할당된다. 만약 인수를 전달하지 않으면 매개변수는 undefined로 초기화된다.
  - 인수는 매개변수에 할당되어질 값을 말한다.

2.  Call-by-value

  - 값을 복사해서 전달하므로 함수 밖은 영향을 미치지 않는다.

    ```js
    function foo(primitive) {
      primitive += 1;
      return primitive;
    }

    var x = 0;

    console.log(foo(x)); // 1
    console.log(x);      // 0
    ```

3. Call-by-reference

   - 참조로 인자를 전달 할 때 값이 변경될 수 있다.

     ```js
     function changeVal(primitive, obj) {
       primitive += 100;
       obj.name = 'Kim';
       obj.gender = 'female';
     }

     var num = 100;
     var obj = {
       name: 'Lee',
       gender: 'male'
     };

     console.log(num); // 100
     console.log(obj); // Object {name: 'Lee', gender: 'male'}

     changeVal(num, obj);

     console.log(num); // 100
     console.log(obj); // Object {name: 'Kim', gender: 'female'}
     ```


### 4. 함수 객체의 프로퍼티

  - 함수는 객체이기 때문에 프로퍼티를 가질 수 있다. 함수는 일반 객체와는 다른 함수만의 표준 프로퍼티를 갖는다.

    ```js
    function square(number) {
      return number * number;
    }
    console.dir(square);
    ```

    - dir()을 사용할 경우 다음과 같은 창을 볼 수 있다.

      ![function property](http://poiemaweb.com/img/function_property.png)

    1. Arguments 프로퍼티

  - arguments 객체는 함수 호출 시 전달된 인수(argument)들의 정보를 담고 있는 순회가능한(iterable) 유사 배열 객체(array-like object)이다. 배열처럼 움직이는 객체를 유사배열객체라고 한다. 번호가 매겨져있는 property를 가지고 있다.

    ```js
    function multiply(x, y) {
      console.log(arguments);
      return x * y;
    }

    multiply();        // {}
    multiply(1);       // { '0': 1 }
    multiply(1, 2);    // { '0': 1, '1': 2 }
    multiply(1, 2, 3); // { '0': 1, '1': 2, '2': 3 }
    ```

  - 내부에서 argument를 보고 for 문을 돌려서 모두 더해서 반환할수 있게해준다.
  - 가변인자함수 : 인자의 갯수를 특정하지 않고 비워둠으로 유연하게 대처한다.

    ```js
    function sum() {
      var res = 0;

      for (var i = 0; i < arguments.length; i++) {
        res += arguments[i];
      }

      return res;
    }

    console.log(sum());        // 0
    console.log(sum(1, 2));    // 3
    console.log(sum(1, 2, 3)); // 6
    ```

    2. caller 프로퍼티

  - 자기 자신을 넣고 호출 call-back 함수를 의미한다.

    ```js
    function foo(func) {
      var res = func();
      return res;
    }

    function bar() {
      return 'caller : ' + bar.caller;
    }

    console.log(foo(bar)); // function foo(func) {...}
    console.log(bar());    // null (browser에서의 실행 결과)
    ```

    3. length 프로퍼티

  - 매개변수의 갯수를 참조하고싶을때 사용함

    ```js
    function foo() {}
    console.log(foo.length); // 0

    function bar(x) {
      return x;
    }
    console.log(bar.length); // 1

    function baz(x, y) {
      return x * y;
    }
    console.log(baz.length); // 2
    ```

  4. name 프로퍼티

    ```js
    // 기명 함수표현식(named function expression)
    var namedFunc = function multiply(a, b) {
    return a * b;
    };
    // 익명 함수표현식(anonymous function expression)
    var anonymousFunc = function(a, b) {
    return a * b;
    };

    console.log(namedFunc.name);     // multiply
    console.log(anonymousFunc.name); // ''
    ```

  5. \__proto__프로퍼티

     > ECMAScript spec에서는 **모든 객체는 자신의 프로토타입을 가리키는 [[Prototype]]이라는 숨겨진 프로퍼티를 가진다** 라고 되어있다. 크롬, 파이어폭스 등에서는 숨겨진 [[Prototype]] 프로퍼티가 __proto__ 프로퍼티로 구현되어 있다. 즉 __proto__과 [[Prototype]]은 같은 개념이다.

     ```js
     function square(number) {
       return number * number;
     }

     console.dir(square);
     ```

     >square() 함수 역시 객체이므로 [[Prototype]] 프로퍼티(__proto__ 프로퍼티)을 가지며 이를 통해 자신의 부모 역할을 하는 프로토타입 객체를 가리킨다.함수의 프로토타입 객체는 `Function.prototype`이며 이것 역시 함수이다.

     ```js
     function square(number) {
       return number * number;
     }

     console.log(square.__proto__ === Function.prototype); //true
     console.log(Object.getPrototypeOf(square) === Function.prototype); //true
     ```

  6.  prototype 프로퍼티

> 자신의 부모역할을 할 객체를 가리킨다. --proto-- 인스턴스 일반객체 자신의 부모역할을 하는 프로퍼티를 가리킨다. 체인관계상 상위에있고 그 위에 object프로퍼티다 .프로토타입의 종점은 object.prototype이다.

- 관계 구조도

![Object literal Prototype chaining](http://poiemaweb.com/img/object_literal_prototype_chaining.png)