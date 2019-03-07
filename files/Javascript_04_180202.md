# Lesson Javascript_04 (180202[Fri])

## JavaScript Fundamental 04

### 1. Javascript Prototype

> 프로토타입의 리소스(프로퍼티)를 공유한다. 생성되는 객체마다 가지는 메서드 내용이 같은것을 구현하기 위해 프로토타입 객체를 공유한다. 
>
> 자바스크립트는 멀티패러다임 언어이다. (명령형, 절차형, 함수형, 프로토타입기반 객체지향)



함수는 생성자 함수로 사용될 가능성이 있기때문에 함수만이 유일하게 prototype객체를 지닌다. 

객체를 생성하는 목적으로 만들어진 함수를 생성자 함수라고한다. 함수명 첫문자를 대문자로 적어 다른 일반함수와 구분한다.

생성자 함수와 일반 함수의 차이점은 new 연산자로 구분한다. 함수가 생성자 함수로 사용되어지는지 확인하기 위해 prototype 프로퍼티를 생성한다.

기명 즉시실행함수(IIFE, Immediately Invoke Function Expression)  별도의 호출을 하지 않고 선언과 동시에 실행한다.



### 2. 생성자함수

- 생성자함수 내부의 프로퍼티와 생성자함수의 prototype 프로퍼티의 동작원리

![constructor function prototype chaining](http://poiemaweb.com/img/constructor_function_prototype_chaining.png)

### 3. 기본자료형의 확장

- string(기본자료형)을 객체화 시켜 immutable한 특성을 mutable하게 바꿀 수 있다. Javascript에 있는 String 생성자 함수를 사용하여 객체화 시킬 수 있으나 구문을 실행하고나서는 다시 기본자료형으로 브라우져가 바꿔 인식한다. 생성자 함수의 객체에 접근하여 객체화 시켜 객체처럼 사용 할 수도 있으나 권장되지 않는 방식이다.



## Scope

#### What is the Scope?

### 1. Global scope

- 글로벌 영역에 변수를 선언하면 모든곳에서 참조 가능한  전역객체(Global Object) window의 프로퍼티이다.

### 2. Non block-level scope

- 함수 코드블럭내부에 있는 변수를 제외한 모든 변수는 전역변수처리된다.

### 3. 암묵적 전역(implied global)

​	함수안에서라도 var 키워드를 생략하고 변수를 선언할 경우 전역 변수화 해버린다.

```js
function foo() {
  x = 1;   // Throws a ReferenceError in "use strict" mode
  var y = 2;
}

foo();

console.log(x); // 1
console.log(y); // ReferenceError: y is not defined
```



## 함수 호출 패턴에 따라 결정되는 This

### 함수 호출 패턴과 this 바인딩

- 함수 호출패턴에 따라 어떤 객체를 this에 바인딩할지 결정된다.

1. 함수 호출 패턴(Function Invocation Pattern)
2. 메소드 호출 패턴(Method Invocation Pattern)
3. 생성자 호출 패턴(Constructor Invocation Pattern)
4. apply 호출 패턴(Apply Invocation Pattern)



#### *오늘 새로 배운 내용들

### 생성자 함수 동작 방식

**1. 빈 객체 생성 및 this 바인딩**

생성자 함수의 코드가 실행되기 전 빈 객체가 생성된다. 이 빈 객체가 생성자 함수가 새로 생성하는 객체이다. 이후 **생성자 함수 내에서 사용되는 this는 이 빈 객체를 가리킨다.** 그리고 생성된 빈 객체는 생성자 함수의 prototype 프로퍼티가 가리키는 객체를 자신의 프로토타입 객체로 설정한다.

**2. this를 통한 프로퍼티 생성**

생성된 빈 객체에 this를 사용하여 동적으로 프로퍼티나 메소드를 생성할 수 있다. this는 새로 생성된 객체를 가리키므로 this를 통해 생성한 프로퍼티와 메소드는 새로 생성된 객체에 추가된다.

**3. 생성된 객체 반환**

- 반환문이 없는 경우, this에 바인딩된 새로 생성한 객체가 반환된다. 명시적으로 this를 반환하여도 결과는 같다.
- 반환문이 this가 아닌 다른 객체를 명시적으로 반환하는 경우, this가 아닌 해당 객체가 반환된다. 이때 this를 반환하지 않은 함수는 생성자 함수로서의 역할을 수행하지 못한다. 따라서 생성자 함수는 반환문을 명시적으로 사용하지 않는다.

```js
var Person = function(name) {
  // 생성자 함수 코드 실행 전 -------- 1
  this.name = name;  // --------- 2
  // 생성된 함수 반환 -------------- 3
}

var me = new Person('Lee');
console.log(me.name);
```



![constructor](http://poiemaweb.com/img/constructor.png)



### ### apply 호출 패턴(Apply Invocation Pattern)

```js
func.apply(thisArg, [argsArray])
// thisArg: 함수 내부의 this에 바인딩할 객체
// argsArray: 함수에 전달할 argument의 배열
```

- apply()를 사용한 this 사용용례 확인

```js
var Person = function (name) {
  this.name = name;
};

var foo = {};

// apply 메소드는 생성자함수 Person을 호출한다. 이때 this에 객체 foo를 바인딩한다.
Person.apply(foo, ['name']);

console.log(foo); // { name: 'name' }
```



* 현재 이해하고 있는 내용과 그 확인

argument는 object의 프로퍼티만 사용가능

Function.prototype 안에 있는 apply 함수는 2개의 인자를 받는데 첫번째 인자로 this를 갈아끼면서 호출하고 뒤에는 argument를 받아서 넣어준다.

apply함수는 .앞에 있는 함수의 this를 갈아끼면서 호출하는 함수이다.