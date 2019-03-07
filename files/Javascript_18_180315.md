# Lesson Javascript_18 (180315[Thu])

## JavaScript Fundamental 18

### Angular Directive

> 디렉티브(Directive 지시자)는 “DOM의 모든 것(모양이나 동작 등)을 관리하기 위한 지시(명령)”이다. HTML 요소 또는 어트리뷰트의 형태로 사용하여 디렉티브가 사용된 요소에게 무언가를 하라는 지시(directive)를 전달한다.

> 컴포넌트는 View를 위해 있다. 다른 컴포넌트의 부품으로도 사용되고 각 컴포넌트와 느슨하게 연결되어 있다. 컴포넌트는 View를 생성하고 관리한다. 가독성과 생산성(유지보수)를 위해 공통된 부분은 Directive로 만들어 다른 컴포넌트가 공통으로 사용할 수 있도록 한다.


- 컴포넌트 디렉티브(Component Directives)
  컴포넌트의 템플릿을 표시하기 위한 디렉티브이다. @component 데코레이터의 메타데이터 객체의 seletor 프로퍼티에서 임의의 디렉티브의 이름을 정의한다.

- 어트리뷰트 디렉티브(Attribute Directives)
  어트리뷰트 디렉티브는 HTML 요소의 어트리뷰트로 사용하여 해당 요소의 모양이나 동작을 제어한다. ngClass, ngStyle와 같은 빌트인 디렉티브가 있다.

    ```ts
    <app-todo *ngIf></app-todo>
    // *ngif와 같은 디렉티브는 app-todo(host요소)를 보이게도 하고 안보이게도 하는 구조적 역할을 지시하는 디렉티브이기 때문에 구조 디렉티브라고 한다.
    ```

- 구조 디렉티브(Structural Directives)
  구조 디렉티브는 DOM 요소를 반복 생성(ngFor), 조건에 의한 추가 또는 제거(ngIf, ngSwitch)를 통해 DOM 레이아웃(layout)을 변경한다.

- 사용자 정의 디렉티브
  사용자 정의 디렉티브는 Angular의 빌트인 디렉티브가 아닌 사용자 정의 디렉티브이다.