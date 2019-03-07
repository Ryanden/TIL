## Lesson 03 (180117)  
## CSS 구조

### 마크업에는 항상 논리적인 구조로 설계

- Image Replacement (컨텐츠는 항상 정보를 넣기)

- 의미를 가지는 컨텐츠와 장식용 컨텐츠는 항상 분리하여 생각하기  
    - h1.log>a[href="#"]>img
    - seo(검색엔진최적화)

## ARIA (Accessible Rich Internet Applications)
 1. 표준
 2. 가이드라인
    1. 인식 (인식체계가 적합한지)
        - 장애에 관계없이 모두가 정보를 동등하게 제공받는것
            1. 대체 텍스트(이미지를 이해할 수 있도록 텍스트도 제공)
            2. 명료성(색에 무관한 컨텐츠로 인식, 명확한(자세한) 지시사항 제공)
            3. 텍스트와 컨텐츠의 명도 대비는 기준이 필요
            4. 자동재생금지(시각장애인의 인식을 방해 )
            5. 이웃한 컨텐츠는 구별될 수 있어야한다
    2. 운용 (운용문제가 없는지)
    3. 이해 (이해하는데 문제가 없는지)
    4. 견고 (신기술이 등장해도 호환가능하게)
    - wai
    - wcag 1.0 / 2.0  
    - kwcag(korean web content accessiblity guidelines) 2.1  

## 입력장치의 접근성
> 고려할 사항들  
    
- 미리 컨텐츠에 대한 이야기를 제시 
- 광과민성 발작예방(과도한 화면반짝임)
- 쉬운 네비게이션   
    (반복되는 항목을 건너뛰기 ) 
    - 본문이 시작하기전에 
    - 적절한 제목을 사용해야한다 
        - 특수문자 사용자제(모든사용자를 고려)
        - 링크텍스트는 용도나 목적을 이해 할 수 있도록 제공해야한다.(여기 or 클릭 같은 용도가 불분명한것을 링크로하는 행동 자제)

    - *Tips 링크의 범위는 최소 width :44px(6mm) height:44px(6mm) 제공 
## 새로배운 CSS 정보

1. 컨텐츠는 남기면서 화면에서 지우기
    - position: absolute;  
    - left: -9999em;
    - clip: rect(0 0 0 0);
    - overflow: hidden;
    - visibility: hidden;
2. 컨텐츠 앞에 가상선택자 삽입방법
    - .member li:nth-child(n+2)::before {content: ":";}
    - 참고:http://nthmaster.com/
3. inherit(상속)을 사용한 font-size조절
    - font-size : inherit;
4. padding과 border을 사용한 layout조절 
    - position: relative;
    - padding: 10px 30px 50px 30px;
    - border-radius: 0 0 15px 15px;
 

