# Lesson 08 (180125)  
## CSS 기능5(실습)


### 내용 숨기기 트릭
1. paddig trick 
```css
.class{
    box-sizing:border-box;
    padding-top:30px;
    overflow:hidden;
    /*box를 border-box타입으로 바꾸고 padding을주고 넘치는 컨텐츠를 overflow를 사용하여 감춤*/
}
```
2. overflow : hidden;
```css
.class{
    overflow: hidden;
    /* content의 영역을 벗어나는 내용은 숨김처리 */
}
```
3. white-space: nowrap;
```css
.class{
    white-space: nowrap;
    /* 줄바꿈을 허용하지 않음*/
    text-indent : 10px;
    /* 첫줄만 들여쓰므로 보통 nowrap과 같이 사용하며 border와 관계없이 글자를 들여쓴다. */
}
```
### cotent 배치 
1. display: flex (구브라우져에서 작동이 안될 수 있음)
```css
.class{
    display: flex;
    justify-content: flex-start;
    align-items: center;
}
```
2. margin-left
```css
.class{
    margin-left: auto;
    /* 남은 margin을 자동으로 배치 */
}
```
3. float
```css
.class{
  float: right;
  position: relative;
  top:5px;
}
```
4. position: absolute
```css
.class{
  position: absolute;
  top:50%;
  right: 0;
  margin-top: -5px;
  /* 음수마진을 사용하여 가운데 배치 %를 사용하여 추후 유지보수에도 유연하게 대처 */
}
```
4. transform: translateY(-50%)
```css
.class{
transform: translateY(-50%);
/* 상자 크기의 y기준으로 크기조절
  이 기능은 모던브라우저에서 사용가능하므로 브라우져가 어디까지 지원하는지 canIuse에서 확인 */
}
```
### 새롭게 배운 CSS기능
1. article
> article요소는 h2와 같은 제목 사용을 권장  
2. blockquote 
> &lt;blockquote&gt; 블락단위로 컨텐츠를 인용했을때 사용
3. cite
> cite="출처" 속성안에 출처를 명시해 줄 수 있음
4. inline요소 배치
- inline요소들을 기준에 맞춰 정렬함
```css
.Class{
    vertical-align :top;
}
```
5. grid-area의 축약형
```css
.class{
 grid-area: 1/2/3/4;
 /* 앞에부터 row-start column-start row-end column-end */
}
```




