# Lecture 02
## 20180116

## What is CSS??

- 스타일링을 위한 언어

## CSS의 과거와 현재

- 1996년에 w3c의 주도하에 Level1 발표  
- 1998년 Level2 등장  

## CSS모듈

>모바일과 데스크톱 브라우져별로 css3test사이트에서 테스트  
>zenGarden을 통해 같은 html에 다양한 스타일링 구현

## Selector
>HTML의 구조를 CSS를 통해 선택
1. 태그의 이름으로 선택
2. 클래스 속성으로 선택  

## CSS3의 브라우저별 접두사(Vendor prefix)
- CSS3의 표준안은 현재 확정되어있지 않아 실험적으로 속성을 제공하고있어 각 브라우져마다 속성 앞에 prefix를 선언하여 사용  

*렌더링엔진에 따라 성능차이가 있다 (webkit등)

## CSS 단위

> (#ff0000 ) 의 경우 RGB의 16진수를 나타내는 #태그와 FF를 활용한 255를 나타내는 숫자 0000은 GB  
- RGBA함수(RGBA인자를 4개받음)  
- HSLA함수(색상(hue),채도,명도,투명도)   
    - Hue값 360도로 색상을 나눠서 사용  

## CSS 적용

- link를 활용하여 적용
- @import를 활용하여 적용

- embeded
- inline (우선순위가 높아 스타일의 당장은 원하는 스타일이 재현 가능할지 모르나 재정의가 어렵고 유지보수가 까다로워 권장하지 않는 방식)

- tree 구조로 생성 DOM

## CSS 상속(Inherit)

## 브라우져마다 agency가달라 기본제공 Font도 달라짐 
- fantasy계열 
- cussive
- monospace
- serif (날카로운 글꼴 궁서체 바탕체)
- sans-serif [generic-family] (고딕체 부드러움)
- *참조(web font gallery) 
- Tips. 글꼴군을 항상 마지막에 명시

spoqa han sans (adobe에서 아시아권을위해 제공한 web font)

## Web Page 제작과정
1. HTML 구조 설계
2. 고정형 / 유동형 [타입설정]
3. 구조에 따른 CSS, Javascripts 제작
4. 디버깅 및 시현

## 레이아웃방식
- float
- flex -> 부모의 디스플레이값을 바꿈 
    - box-sizing : border-box (margin + width or height (padding + border)) 너비
- grid
- position

## Code 단축키
- alt+ 방향키 (한줄이동)
- ctrl+ / (한줄주석)
- ctrl+ shift+ k (한줄삭제)
- ctrl+ shift+ d (전코드복제)
