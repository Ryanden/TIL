# 0115 Html 
## 기본환경조성

>확장프로그램설치  

1. web develope  
2. open wax  
3. headingsmap

## HTML4의 약점
- 문법의 간략화  
- 대소문자 구분하지않음

## XHTML의 등장
XHTML (html4와 xhtml의 문법은 동일하나 규칙의 차이가있음)  
규칙을 더엄격하게 적용하여 표준화함
앞뒤를 마크업해주어 컨텐츠를 바로 확인

## 그 이후
w3c의 xhtml 1.0이후 2.0작업이 진행되었으나,   하위 호환성의 문제가 발견되어 WHATWG에서 Web Forms2.0이라는 표준을 만듦

컨텐츠에 의미를 부여함(Mark up)
HTML5는 각각의 밴더들이 어플리케이션을 개발하기위해 모여서 표준을 만들자 w3c가 실패를 인정하고 표준화를 따라 HTML5를 만듦

## What is dtd?
Transinal.dtd(여러가지명령어 사용가능, 하위호환성 좋음)  

Strict.dtd (의미를가지는 구조만 허용함, 
엄격한구조만허용)  

Frameset.dtd ( 5에선 사용안함)  

## Rendering Type
Standard Mode : 렌더링싱자 px 포함안함 120px
Qux(쿽스) Mode : 렌더링상자의 px을 포함 100px

Document object Mode(DOM)

속성중복선언 불가

## 4.1과 1.0의 특징
> *Block VS Inline  

독립적으로 하나씩 자리를 차지함 (block 엘리먼트)
image와 a태그는 inline임 블록이 인라인을 포함해야함

html5에서는
위와같은 규칙이 느슨해짐 인라인이 블록 포함가능

section : 자신의 부모section을 따라 컨텐츠의 구조를 파악
article
aside
nav
*상위 4개는 제목이 필요함

> API 
- application cache (인터넷이 끊어져도 다운로드 받은 peed를 활용하여 한정된 관람가능)
- web workers(오프라인에서 유용)
- Geolocation(구글맵)
- Device Orientation(핸드폰기울기센서(게임))

> 병렬방식의 HTML제작 및 CSS스타일링
- 3단구조 or 4단구조
    - 3단 : 헤더 / 컨텐츠 / 푸터
    - 4단 : 헤더 / 네비(헤더분리) / 컨텐츠 / 푸터
> Naming_Standard  

PC (Pascal case) 앞단어를 대문자
CC (Camel case) 뒤단어를 대문자
KC (Kebab case) -을이용하여 두단어
