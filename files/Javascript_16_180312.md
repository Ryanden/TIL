# Lesson Javascript_16 (180312[Mon])

## JavaScript Fundamental 16

### Angular Template

- ​데이터 바인딩
  - 인터폴레이션(Interpolation)
  - 프로퍼티 바인딩(Property binding)
  - 어트리뷰트 바인딩(Attribute binding)
  - 클래스 바인딩(Class binding)
  - 스타일 바인딩(Style binding)
  - 이벤트 바인딩(Event binding)
  - 양방향 데이터 바인딩(Two-way binding)
- 빌트인 디렉티브(Built-in directive)
  - 빌트인 어트리뷰트 디렉티브(Built-in attribute directive)
    - ngClass
    - ngStyle
  - 빌트인 구조 디렉티브(Built-in structural directive)
    - ngIf
    - ngFor
    - ngSwitch
- 템플릿 참조 변수(Template reference variable)
- 템플릿 표현식 연산자(Template expression operator)

###Data Binding

- Model과 View를 분리한다. 

- 관심사가 다른것은 분리한다.

- J-Query의 DOM조작 프로그래밍

  ![procedural-programming](http://poiemaweb.com/img/procedural-programming.png)

####HTML

- 구조를 형성하고 데이터를 배열하는 '선언형프로그래밍'방식이다.

- 기존 Javascript에서 Dom에 접근하여 HTML을 수정했다면, Template에서 Component Class로 접근하여 HTML을 수정한다.

  ![declarative-programming](http://poiemaweb.com/img/declarative-programming.png)

- 느슨한 구조로 application을 만드는것이 특징이다.

#### 변화감지(Change Detection)

> Data Binding을 위해 사용되어진다. Template과 Component의 클래스 변화를 감지한다.

#####Model의 변화감지

- Event 발생
- AJAX 통신발생
- 타이머함수발생

##### Zone.js의 몽키패치

- 기존에 있는 메서드에 사용자정의 메서드를 프록시(proxy)하여 사용자정의 메서드를 호출하고 기존의 메서드의 기능을 빌려 사용한다.

  ```js
  function zoneAwareAddEventListener() {...}
  function zoneAwareRemoveEventListener() {...}
  function patchTimer() {...}
  function zoneAwarePromise() {...}
  ...

  window.prototype.addEventListener = zoneAwareAddEventListener;
  window.prototype.removeEventListener = zoneAwareRemoveEventListener;
  window.prototype.promise = zoneAwarePromise;
  window.prototype.setTimeout = patchTimeout;
  ...
  ```

#### Angular의 데이터 바인딩

| 데이터 바인딩        | 데이터의 흐름            | 문법                               |
| -------------------- | ------------------------ | ---------------------------------- |
| 인터폴레이션         | 컴포넌트 클래스 ⟹ 템플릿 | {{ expression }}                   |
| 프로퍼티 바인딩      | 컴포넌트 클래스 ⟹ 템플릿 | [property]=”expression”            |
| 어트리뷰트 바인딩    | 컴포넌트 클래스 ⟹ 템플릿 | [attr.attribute-name]=”expression” |
| 클래스 바인딩        | 컴포넌트 클래스 ⟹ 템플릿 | [class.class-name]=”expression”    |
| 스타일 바인딩        | 컴포넌트 클래스 ⟹ 템플릿 | [style.style-name]=”expression”    |
| 이벤트 바인딩        | 컴포넌트 클래스 ⟸ 템플릿 | (event)=”statement”                |
| 양방향 데이터 바인딩 | 컴포넌트 클래스 ⟺ 템플릿 | [(ngModel)]=”variable”             |