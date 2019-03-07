# Lesson Javascript_19 (180320[Tue])

## JavaScript Fundamental 19

### Angular Service

공통기능을 분리하여 관심사가 Logic과 관련이 있는것들은 service로 분리한다.

서비스의 생성

- Framework가 사용자가 요청할때 인스턴스를 컴포넌트에 주입해준다.

  ```ts
  // greeting.service.ts
  import { Injectable } from '@angular/core';

  @Injectable()
  export class GreetingService {
    sayHi() { return 'Hi!'; }
  }
  ```

  ​



- 긴밀한 연결은 Anti pattern이다

  ```ts
  // app.component.ts
  import { Component } from '@angular/core';
  // 컴포넌트에서 사용할 서비스를 임포트
  import { GreetingService } from './greeting.service';

  @Component({
    selector: 'app-root',
    template: `
      <button (click)="sayHi()">Say Hi</button>
      <p>{{ greeting }}</p>
    `
  })
  export class AppComponent {
    greeting: string;
    // 서비스의 인스턴스를 담을 프로퍼티
    greetingService: GreetingService;

    constructor() {
      // 서비스의 인스턴스의 명시적 생성
      this.greetingService = new GreetingService();
    }

    sayHi() {
      // 서비스의 사용
      this.greeting = this.greetingService.sayHi();
    }
  }
  ```

- appcomponent는 greeting이라는 클래스가 필요하다. 의존적인 관계이다. npm의 dependency도 필요한 관계이기 때문에 의존관계이다.

![dependency](http://poiemaweb.com/img/dependency.png)

- B는 A에 의존하고 있기 때문에 A가 바뀌면 B도 같이 수정되어야 한다. 이러한 긴밀한 관계는 유지보수에 악영향을 준다.

#### 의존성주입

> 상기의 문제를 해결하기 위하여 나온 것이 의존성 주입(Dependency Injection)이하 D.I라고한다.

어떻게 의존성을 생성하는가 어떤 의존성을 외부의 설정으로 분리할 것인가



### Reactive Programming과 RxJS

1. 비동기 데이터의 처리
   - promise
   - generate
   - asynchronous await
   - reactive programing
2. input
   - 배열 (동기)
   - 함수 (동기)
   - AJAX (비동기)
   - Event(비동기)
3. 비동기와 동기 모두 동일한 방법으로 데이터를 처리하고 싶어서 나오는 방법