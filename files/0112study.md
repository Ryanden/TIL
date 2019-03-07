# 0111 복습
>cookie와 session의 차이

cookie는 로컬
session은 log가 서버에남음 
-활성화된 시점을 30분으로 둠
열려있는 세션에 다시 연결시켜줌
네이버로그인할때 재로그인하지않고 연결이가능

TCP와 UDP의 차이

OSI 7Layers가

Socket

# Web Programing

웹개발 프로그래밍의 변화
cerl 
문서조회
>1991~1999 하이퍼텍스트기반의프로젝트를 만듦

정적인 컨텐츠
한페이지마다 컨텐츠가 필수
내용이 바뀔수 없음

- 동적인 컨텐츠<탬플릿>

네이버 글쓰기같은
배경/색깔등 구조는 존재하는상태
database에서 정보를 호출하여 정보를 
내용만바꿈

힉스입자 

lamp스택(linux apache mysql php)리눅스와 php가 안정적으로 돌아가게 페이지를 관리 linux apache로 데이터관리

하나의 레이아웃으로 데이터베이스정보를 조회하여 컨텐츠만 바꿈
- 1999~2009
뒤에서 컨텐츠를 그려서 전달
- 2010~현재
이제는 내용을 받아서 그려서 전달

1세대 수억개의 html파일존재
2세대 템플릿페이지한개를 만들어 DB에서 HTML을 조합하여 보냄
서버가 html을 다만들어진것을 전달

3세대 자바스크립트를이용하여 vue를통해 사용자쿠키를분석하여 사용자의 이름을 게시하는게 가능
html 내용만전달함
동적으로 전반부에서 정보변경가능
---
## Web Browser

파싱

구조를 그림으로 바꿔내는게 렌더링

### Mosaic
웹브라우져의 조상
netscape의 nevigater

javascript v8엔진
3세대 개발을 가능하게함

크로미움기반 브라우져 (크롬개발자용)
비발디브라우져
- 4대 브라우져
크롬 파이어폭스 엣지 사파리

>크롬개발자들의 회의

- progressive web app
웹페이지를 앱처럼
푸시를날림 오프라인사용가능
서비스워커라는 도구를 사용함
구글 크롬 vs 구글 안드로이드
amp와 pwa 

opengl(웹에서3d를그림)


서비스웹
다크웹(결제쳬계 비트코인)

## Web architecture
> 클라이언트요청 > 서버응답

engineX
톰켓 아파치

장고개발자

mvc(Model view Controller)패턴

여러개의 모듈을 합침

mvw(Angular)방식 

많이쓰는 기능들을 모아둔것(framework)

getuikit.com

purecss[그리드시스템제공]

공약수가많은 12등분으로 그리드가 많이 짜여짐.

## Server-side
- 언어에따라 달라짐
    - javaScript

## Database
- RDBMS(스프레드시트)

- noSQL(정보를모아 하나의파일)

## Etc
- 그외에 배포하기 위한 것들
    - github, bitbucket 등


## URI, URL, URN
    어떤자료를 (application layer)
    통신방식을 결정함(https)
    www(www방식)

프로토콜/도메인/path/파일명

## API

응용프로그램이 운영체제를 통해 정보를 잘 전달하게 하기 위한 중간 인터페이스(kennel)

## web API

- REST(API)
SOAP()

https://github.com/ulgoon/wps-se/blob/master/handouts/fds-se-5-network(2).md

## summary (12.Feb Days 5)

- Web programming  
        - 3단계 구성

- Web Browser

- URI / URL 의차이

    - URI 모든정보를 포함(프로토콜/도메인/path/파일명)
    - URL
    (Locator정보까지만 가짐(파일명제외))

- REST API
어떤방식으로 정보를 요청하고 받는지    
pros : 주소로 정보 요청가능  
cons : 사용 메소드 4개
       표준이 없다

- Web architecture

    - client와 server가 하는일의구분
        - Client
        - Server
        - Business Layer
        - Data base





