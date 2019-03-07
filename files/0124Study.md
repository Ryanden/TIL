# Lesson 08 (180124)  
## CSS 기능4(실습)

### 접근성(견고성)
1. 열고 닫음 태그의 생략하면 안된다.
2. 중첩 관계 선언에 오류가 있으면 안된다.
3. 속성 선언을 중복 선언해서는 안된다.
4. id 속성의 중복사용 금지  
    - id를 꼭 사용해야하는 곳은 어디인가?  
        - fieldset과 같은 form태그

### 새로알게된 CSS정보
1. selector
```css
.class + a{
/* 인접형제 다음 형제까지 선택 */
}
.class ~ a{
/* 뒤에 오는것 전부 선택*/
}
```
2. transition property example
```css
.class{
border: 1px solid #aaa;
border-radius: 5px;
margin-top: 10px;
background-color: #fff;
height: 27px;
overflow: hidden;
transition: height 0.5s padding 0.5s;
}
.class:hover{
height: 137px;
padding: 5px 0;
}
```
3. transition additional example
```css
transition: height 0.5s, padding 0.5s;
transition-property: height, padding, background;
transition-property: all;
transition-duration: 1s;
transition-delay: 0s, 1s, 2s;
transition-timing-function: ease-in-out;
/* transition-property: 높이 플레이시간 딜레이시간 */
transition-timing-function: ease-in-out;
/* 감속 가속 감속 */
```
4. transform property example
```css
.class{
  margin-top:20px;
  background: #ff0;
  border: 10px solid #000;
  border-radius: 50%;
  width: 180px;
  height: 180px;
  text-align: center;
  line-height: 160px;
  transform: rotate(0deg) scale(1) skew(0deg);
  transition: transform .5s;
}

.class:hover{
  transform: rotate(360deg) scale(0.7) skew(-15deg) ;
}
```
- 컨텐츠박스 : 디포트설정 
- 보더박스 : 위아래 마진이 포함됨
- line-height
- text-align
- decender영역  블록으로 만듦

### CSS사용시 Process
1. border로 벽지 만들기
- example
```css
.class{
border: 1px solid #aaa;
border-radius: 5px;
padding: 10px;
background:linear-gradient(to bottom), #eee, #ccc;
background-color: #ccc;
position: relative;
}
```
2. layout설정
```css
.class{
    margin:10px;
    padding:20px;
    position:relative;
}

.class img{
    position:absolute; 
    /* absolute를 사용시 선택한 컨텐츠를 layer화 시키는데 여기서 상위 목록에 postion:relative가 없을 경우 (기준점이없을경우) 기준점을 찾을때까지 올라가다가 없을 경우 사라질 수 있으니 postion:absolute를 사용시엔 반드시 상위목록에 postion:relative를 명시해줄것! */
}
```
3. 본인이 만든 HTML의 문서가 오류가 있지 않은지 확인한다 
>https://validator.w3.org/   
상위 사이트로 접속하여 본인이 만든 .html 문서를 업로드하여 확인

4. 각요소를 선택하여 draft에 따라 배치
>HTML을 통한 마크업이 끝나고 css를 할때엔 자신이 적절한 선택자를 사용하고 있는지 확인 한다. 브라우져를 통해 확인하는 것이 빠르다.

5. CSS파일 확인 
> CSS작업이 끝났으면 CSS에 1차 작업이 끝나고 육안으로 문제가 없다고 판단이서면 http://jigsaw.w3.org/css-validator/  
상위 사이트로 접속하여 본인이 만든 .css 문서를 업로드하여 확인



    



  
