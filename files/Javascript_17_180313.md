# Lesson Javascript_17 (180313[Tue])

## JavaScript Fundamental 17

### Angular Template reference variable & Safe navigation operator

##### 1. 템플릿 참조변수(Template reference variable)

> 템플릿 참조 변수는 DOM 요소에 대한 참조를 담고 있는 변수이다. 템플릿의 요소 내에서 해시 기호(#)를 변수명 앞에 추가하여 템플릿 참조 변수를 선언하고 템플릿 내 자바스크립트 코드에서는 해시 기호없이 참조한다. 템플릿 참조 변수는 템플릿 내에서만 유효하며 컴포넌트 클래스에 어떠한 부수 효과(Side effect)도 주지 않는다. 하지만 템플릿 참조 변수의 값을 이벤트 바인딩을 통해 컴포넌트 클래스로 전달할 수는 있다.

##### 2. Safe navigation operator

> 세이프 내비게이션 연산자 `?`는 컴포넌트 클래스의 프로퍼티의 값이 null 또는 undefined일 때 발생하는 에러를 회피하기 위해 사용한다.

```ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <!-- obj가 null 또는 undefined일 때 아무것도 표시하지 않는다. -->
    {{ obj }}
    <!-- ERROR TypeError: Cannot read property 'id' of undefined -->
    {{ obj.id }}
    <!-- 세이프 내비게이션 연산자는 null 또는 undefined의 프로퍼티를 만나면 처리를 종료하고 에러를 발생시키지 않는다. -->
    {{ obj?.id }}
  `
})
export class AppComponent { }
```

#### 컴포넌트 간의 상태 공유(Component-interaction)

> Angular 애플리케이션은 컴포넌트를 중심(CBD, Component Based Development)으로 구성된다. 컴포넌트는 재사용이 용이한 구조로 분할하여 작성하며 이렇게 분할된 컴포넌트를 조립하여 가능한 중복없이 UI를 생성한다. 컴포넌트는 독립적인 존재이지만 다른 컴포넌트와 결합도를 낮게 유지하면서 다른 컴포넌트와 상태 정보를 교환할 수 있어야 한다.
>

![component-interaction](http://poiemaweb.com/img/component-interaction.png)

- @Input, @Output 데코레이터
- ViewChild와 ViewChildren
- 서비스 중재자 패턴을 구현한 상태 공유 서비스
- 상태 관리를 위한 외부 라이브러리(NgRx, Redux 등) 사용

#### 2. 부모 컴포넌트와 자식 컴포넌트의 상태 공유

> form 요소를 가지고 있는 부모 컴포넌트의 경우, 사용자에 의해 상태(state)가 변경되면 이를 자식 컴포넌트와 공유할 필요가 있다. 이러한 경우 부모 컴포넌트는 **프로퍼티 바인딩**을 통해 자식 컴포넌트에게 상태 정보를 전달한다. 자식 컴포넌트는 부모 컴포넌트가 전달한 상태 정보를 **@Input 데코레이터**를 통해 컴포넌트 프로퍼티(입력 프로퍼티)에 바인딩한다.

![parent to child](http://poiemaweb.com/img/parenttochild.png)

- 자식컴포넌트는 부모컴포넌트의 data정보와 type의 정보만 알 수 있으며 느슨한 결속이 형성된다.



stateful component(event담당, 비순수)  & stateless component(rendering 담당, 상태를 알려줌, 순수)
