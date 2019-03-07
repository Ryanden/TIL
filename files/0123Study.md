# Lesson 07 (180123)  
## CSS 기능4(실습)


### WAI-ARIA
>접근성에 대한 ARIA규칙

### CSS의 Element정리

1. position (이하의 property들은 postion element가 정의 된 이후 사용이 가능하다)
    1. static
        - static은 정적인 property이다. 
        - 프로퍼티 설정이후 top, bottom, left, right등으로 위치를 조정 할 수 없다.
        - 블락형태로 지정하지 않으면 default값으로 영역을 차지한다.
        - border 등의 프로퍼티는 사용이 가능하다.
    2. relative
    3. absolute
    4. fixed
        - fixed는 화면에 고정시키는 property이다
    5. sticky
        - 스크롤을 내려도 컨텐츠가 가장위에 붙어서 따라다닌다.
    6. overlapping
        -zindex :-1 을 사용하여 두개 이상의 컨텐츠를 겹치게 표현한다.
### 새롭게 알게된 CSS기능
- padding: 위 왼쪽 오른쪽 아래  
- 0.5em 상속받은값 x 0.5배  
- 요소선택자 (클래스명 요소 ex) .class element  
- 높이가 가장 높은 인라인상자 기준으로 vertical-align : top  
- padding: 위아래 좌우; 두개를 같이할 경우
- position : absolue 가운데 내용을 없는걸로
- 한줄일때 말줄임 표현 사용을 위해선3가지를 모두 사용해야함
    - white-space: nowrap;
    - overflow: hidden;
    - text-overflow: ellipsis;
- article태그(뉴스)
- figure(caption을 삽입할만한 내용)
  - 사진이나 표 비디오등
  - figcaption이 충분히 내용이 있다면 img alt에 공백표현이 가능하나 그외엔 alt를 자세히 명시할것

