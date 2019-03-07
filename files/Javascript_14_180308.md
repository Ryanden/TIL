# Lesson Javascript_14 (180308[Thu])

## JavaScript Fundamental 14

### Type Script

#### Introduction

- 기존 HTML5가 등장하기 전까지는 Flash, Silverlight, ActiveX등 브라우저에 plug-in에 의존하여 웹페이지를 구축하였다.
- 원할한 웹페이지를 사용하기 위해선 복수의 plug-in을 설치해야하만 하는 불편함이 동반되었다.
- 이러한 문제점을 해결하기 위한 노력으로 HTML5에서는 Javascript만을 이용하여 모든 plug-in을 대체하였다.

> 모든 프로그래밍 언어는 좋은 점과 나쁜 점을 모두 가지고 있다. JavaScript도 언어가 잘 정제되기 이전에 서둘러 출시된 문제와 과거 웹페이지의 보조적인 기능을 수행하기 위해 한정적인 용도로 만들어진 **태생적 한계**로 좋은 점도, 나쁜 점도 많은 것이 사실이다.

- Prototype-based Object Oriented Language
- Scope와 this
- 동적 타입(dynamic typed) 언어 혹은 느슨한 타입(loosely typed) 언어


##### 상기와 같은 Javascript의 태생적 한계를 극복하기 위하여  CoffeeScript, Dart, Haxe와 같은 AltJS(JavaScript의 대체언어)가 등장하였다.

- TypeScript 또한 AltJS의 하나로  JavaScript(ES5)의 Superset(상위확장)이다.

![typescript superset](http://poiemaweb.com/img/typescript-superset.png)



#### Typescript를 사용하는 이유

1. 정적타입

   - 데이터타입을 정하여 함수를 정의하면 오류처리가 빨라지고 가독성이 좋아진다.
   - 런타임 에러를 미리 감지할 수 있다.

   ```ts
   function sum(a: number, b: number) {
     return a + b;
   }

   sum('x', 'y'); // error TS2345: Argument of type '"x"' is not assignable to parameter of type 'number'.
   ```

2. 도구의 지원

   - IDE(통합개발환경)을 포함한 다양한 도구의 지원을 받을 수 있다. IDE와 같은 도구에 타입 정보를 제공 함으로써 타입체크, 리팩토링, IntelliSense등 다양한 지원을 받을 수 있어 생산성이 극대화되기 때문에 프로젝트 진행에 필수적 요소이다.

3. 강력한 OOP지원

   - 인터페이스,제네릭등과 같은 강력한 OOP지원은 프로젝트 코드기반을 쉽게 구성가능하여 OOP언어에 익숙한 개발자의 진입장벽을 낮추는데 큰 효과를 갖는다.

4. ES6 / ES Next지원

   - 컴파일러등의 개발환경 구축이 필요없이, 브라우저만 있으면 바로 사용할 수 있는 ES5와 비교해서 몇 브라우저는 ES6를 완벽지원하지 않아 babel과 같은 트랜스파일러를 사용해야 하는데 Typescript는 ES6를 완벽지원하며 향후 ES모든 버전을 커버하기 때문에 매우 유용하다고 할 수 있다. 

5. Angular

   - 많은 문서들과 예제가 Typescript를 사용하고 잇기때문에 꼭 공부가 필요하다.

#### Typescript의 사용

##### 타입선언

- Typescript는 아래와 같이 변수명뒤에 타입을 명시하는것으로 변수를 선언한다.

  ```ts
  let foo: string = 'hello';
  let bar: number = true; // error TS2322: Type 'true' is not assignable to type 'number'.

  ```

- 선언한 타입에 맞지 않는 값을 할당할경우엔 에러가 발생한다.

#### webpack의기능

1. 라이브러리를 사용하여 export와 import기능으로 모듈들을 실행시켜준다.
2. babel은 모듈로더의 기능이 없고 트랜스파일링해주는 툴이다. 다양한 툴들을 한번에 실해 할 수 있도록 하는 task manager역할을 해준다
3. 여러개의 js파일과 css, img, font, text파일들을 하나로 엮어 실행 시켜준다. 즉, 번들러 역할(모듈번들러)을 한다.

- 브라우저는 모듈 로더 기능이 없기 때문에 webpack을 사용해야한다. typescript는 기존 babel과 역할과 export와 import기능도 대체가능하다.