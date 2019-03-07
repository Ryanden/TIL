# Lesson Javascript_06 (180206[Tue])

## JavaScript Fundamental 06

### 1. 기본자료형(number)를 위한 레퍼(wrapper) 객체

- 기본자료형을 객체처럼 사용하려는 코드를 엔진이 해석하면 순간 기본자료형(number)인 변수를 순간  wrapping하여 객체화하고 프로토타입 객체를 공유하게 된다.
- 프로토타입으로 객체를 만든 이유는 서로 동일한 객체를 공유하여 사용하기 위해서이다.
- 일반메서드의 정의는 생성자함수 내부의 this에 있다.
- 실체는 생성된 객체 내부에 있다.

생성자함수 만들때 (new를 사용 할때)

- 1.  빈객체 생성 
  2.  this는 window를 가리키고있다
  3.  생성된 객체와 윈도우를 묶는다 (바인딩)
  4.  빈객체에 생성될 프로퍼티들을 넣는다.
  5.  빈객체를 리턴하여 인스턴스를 만든다.
- 실수를 2진수로 바꾸면 딱나누어 떨어지지 않는다. 


```js
console.log(0.1 + 0.2);        // 0.30000000000000004
console.log(0.1 + 0.2 == 0.3); // false!!!

function isEqual(a, b){
  // Math.abs는 절댓값을 반환한다.
  // 즉 a와 b의 차이가 JavaScript에서 표현할 수 있는 가장 작은 수인 Number.EPSILON보다 작으면 같은 수로 인정할 수 있다.
  return Math.abs(a - b) < Number.EPSILON;
}

console.log(isEqual(0.1 + 0.2, 0.3));
```



- 전역에 있는 isFinite()와 Number.isFinite()는 실체가 다르다. 전역은 자동형변환을하지만 number는 엄격하게 인수를 받고 자동 형변환을 하지않는다.
- Number.prototype.toFixed()
- 매개변수로 지정된 소숫점 자리를 반올림하여 문자열로 반환. 반환값이 문자열이라는 점에 주의



