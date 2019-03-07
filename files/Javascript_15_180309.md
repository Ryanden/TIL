# Lesson Javascript_15 (180309[Fri])

## JavaScript Fundamental 15

### Angular

#### Introduction

Angular는 Webpage를 Application 처럼 보이게 하기 위하여 SPA개발을 위한 구글의 오픈소스 Javascript Framework이다. 초기 2012년 AngularJS(v1)이 공개되고 후속버전으로 2016년에는 Angular(v2)가 공개 되었고, 2017년 에는Angular(v5)가 출시 되었다. 

##### Angular의 특징

- Typescript를 사용하며 기존 AngularJS의 양방향 데이터 바인딩을 지원하지 않으며 선택적 바인딩을 지원한다.
- 강력한 개발환경지원 도구인 Angular CLI를 제공한다.
- 컴포넌트기반 개발 (CBD, Component Based Development)로 만들어졌다. 

##### Angular의 장점

- Digest Loop로 인한 성능저하 문제 해결. 양방형 바인딩을 하면 watcher가 늘어나게 되는데 watcher의 증대는 트래픽증가를 일으키고 이는 곧 성능저하 문제로 연결된다. 
- AoT (ahead of time compilation)컴파일 사전에 컴파일을 하여 성능저하 문제를 해결. nglf, ngfor, ngswitch와 같은 구조 디렉티브를 브라우저가 실행가능한 코드로 변경해야 하는데 이러한 과정을 런타임에 실시 하지 않고 사전에 컴파일 하기 때문에 AngularJS보다 Framework크기를 50% 가까이 줄일 수 있다.
- Lazy Loading :  SPA방식의 태생적인 문제인 초기 로딩시간문제를 해결하기 위해 필요한 모듈만을 필요한 시점에 로딩하여 성능저하 문제를 해결한다.
- 지속적인 코드 최적화 작업이 진행되고 있어 kb단위로 용량이 줄어들고 있다.

##### Angular CLI

> Angular는 간단한 명령어를 사용하여 Angular 프로젝트 스캐폴딩(scaffolding)을 생성,실행 및 빌드가 가능하다. 

- ng new [project-name]


- ng generate component [component-name]
- ng serve [component-name] -o



##### Angular Component

> 컴포넌트는 Angular의 핵심 구성 요소로서 Angular 애플리케이션은 컴포넌트를 중심(CBD, Component Based Development)으로 구성된다. 컴포넌트의 역할은 애플리케이션의 화면을 구성하는 **뷰(View)**를 생성하고 관리하는 것이다.

1. Web Component

   - 기존의 OOP의경우 로직을 클래스 단위로 분할 할 수 있으나 view를 OOP형태로 분리하는데에는 어려움이 있었다. CSS 자체의 특성때문에 다른 부분에도 영향을 주기 때문이다. 이러한 문제를 해결 하기 위해 Web도 View를 Component단위로 나누어 스코프 단위로, Dom도 Capsule화가 가능 하기위한 노력을 시작 한것이다.

     1. 컴포넌트의 뷰를 생성할 수 있어야 하며(HTML Template)
     2. 외부로부터의 간섭을 제어하기 위해 스코프(scope)를 분리하여 DOM을 캡슐화(Encapsulation)할 수 있어야 하며(Shadow DOM
     3. 외부에서 컴포넌트를 호출할 수 있어야 하고(HTML import)
     4. 컴포넌트를 명시적으로 호출하기 위한 명칭(alias)을 선언하여 마치 HTML 요소와 같이 사용할 수 있어야 한다(Custom Element).

     ​

2. 컴포넌트 트리

   - 어떤 화면이라도 컴포넌트 하나로 생성하고 관리 할 수 있다. 

     ![component tree](http://poiemaweb.com/img/component-tree.png)

     서로간의 컴포넌트가 동일한 부분이 있다면 비슷한 부분은 상위 컴포넌트로 묶고 형제 레벨의 컴포넌트는 루트 밑으로 묶는다. 서로간의 데이터를 참고 해야 할 경우에는 트리 구조에 따라 서로 정보를 참조 할 수 있다.

3. 컴포넌트의 기본동작구조

   ![data binding](http://poiemaweb.com/img/data-binding.png)

   - export class Appcomponent 에서는view를 만들어주는 모든 일을 한다. view는 상태와 data를 가지고 있다. 모델 즉, class는 상태를 감지하고 관리하여 data를 저장하거나 이벤트를 발생시킨다. view와 model은 서로의 변화를 감지하여 서로 동기화하고 상태를 공유한다.

   - 데이터바인딩 (컴포넌트 기본동작구조)

     ![component](http://poiemaweb.com/img/component.png)

   > #####템플릿

   > 컴포넌트의 뷰를 생성하기 위해 HTML과 Angular의 고유한 템플릿 문법(Template Syntax)로 작성된 코드이다.

   > #####메타데이터

   > 컴포넌트 설정 정보를 담고 있는 객체이다. @Component 데코레이터는 메타데이터 객체를 인자로 전달받아서 컴포넌트 클래스에 반영한다.

   > #####컴포넌트 클래스

   > 컴포넌트의 뷰를 생성하는 템플릿의 상태(state)를 관리한다. 데이터 바인딩(Data Binding)을 통해 템플릿에 필요한 데이터를 제공하거나 템플릿에서 발생한 이벤트를 처리한다.

4. 컴포넌트 클래스와 탬플릿의 연동

   ![template-class](http://poiemaweb.com/img/template-class.png)

   - 1번에서 상태변화를 감지하고 2번으로 데이터를 넘기고 3번으로 데이터를 넘기면 변화를 감지하고 바로 view를 바꾸어준다.



##### 템플릿

>템플릿은 HTML과 Angular 고유의 템플릿 문법(Template Syntax)을 사용하여 UI의 최소 단위인 컴포넌트의 뷰를 정의한다. 동적으로 변하는 데이터는 컴포넌트 클래스가 관리하며 템플릿 문법의 데이터 바인딩에 의해 정적 HTML에 포함된다.

##### Angular의 뷰와 모델

![angular-view-model](http://poiemaweb.com/img/angular-view-model.png)

- DOM은 상태(state. 예를 들어 input요소에 값을 입력한 상태 또는 checkbox요소를 체크한 상태)를 가지고 있으며 이 상태는 변화하는 살아있는 것이다. 비록 뷰와 모델은 분리되어 있지만 상태는 공유되어야 한다.

  DOM의 상태가 변화하면 템플릿은 변화를 감지하고 변화된 상태를 컴포넌트 클래스로 전달한다. 이때 컴포넌트 클래스는 비즈니스 로직을 실행하고 템플릿에 실행 결과를 공유한다. 템플릿은 이를 전달받아 DOM을 업데이트한다.

- 이전의 웹 애플리케이션은 DOM을 직접 조작하는 방식으로 동작하지만 템플릿은 선언형 프로그래밍(Declarative programming) 방식으로 뷰와 모델의 관계를 관리한다. Angular는 변화 감지(Change detection) 메커니즘 위에서 동작하는 데이터 바인딩(Data binding)을 통해 템플릿과 컴포넌트 클래스를 긴밀히 연결하고 동기화를 유지한다.

![databinding & change detection](http://poiemaweb.com/img/databinding-changedetection.png)

spa방식은 초기에 클라이언트로 파일을통째로 받아 ajax방식으로 필요한데이터만 db에서 가져온다. ajax는 주소창의 url을 변경하지 않는다.

