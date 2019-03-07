# Lesson Activity_01 (180130)  
## JavaScript Flow control Example

### for(제어문) 문제풀이
1. for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.


2. for문을 사용하여 0부터 10미만의 정수 중에서 홀수만을 작은 수부터 문자열로 출력하시오.
    - 2-1 for문을 사용하여 0부터 10미만의 정수 중에서 홀수만을 큰수부터 출력하시오.

3. while문을 사용하여 0부터 10까지 정수 중에서 짝수만을 작은 수부터 출력하시오.

4. while문을 사용하여 0부터 10미만의 정수 중에서 홀수만을 큰수부터 출력하시오.

5. for 문을 사용하여 0부터 10미만의 정수의 합을 출력하시오

6. 1부터 20까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.

7. 1부터 20까지의 정수 중에서 2 또는 3의 배수인 수의 총합을 구하시오.

8. 두 개의 주사위를 던졌을 때, 눈의 합이 6이 되는 모든 경우의 수를 출력하는 코드를 작성하시오.

9. 삼각형출력하기

> 다음을 참고하여 *(별)로 높이가 5인(var line = 5) 삼각형을 문자열로 완성하라.

```javascript
*
**
***
****
*****
```

10. 트리 출력하기
> 다음을 참고하여 *(별)로 트리를 문자열로 완성하라.

```javascript
*
**
***
*
**
***
****
*****
```


### 문제풀이
```javascript
//#region 문제1번함수
function state1() {
    for (var i = 0; i < 10; i++) {
        if (i % 2 === 0)
            console.log(i);
    }
}
state1();
//#endregion
//#region 문제2번함수
function state2(){
    for (var i = 10; i >= 0; i--) {
        if (i % 2 !== 0)
            console.log(i);
    }
}
state2();
function state2_1(){
    var result = '';
    for(var i =0; i<10; i++){
        if(i%2 !== 0){
            result += i;
        }
    }
    console.log(result);
}
state2_1();
//#endregion
//#region 문제3번함수
function state3(){
    var i=0;
    while (i<11) {
        if (i % 2 === 0) {
            console.log(i);
        }
        i++;
    }
}
state3();
//#endregion
//#region 문제4번함수
function state4() {
    var i = 10;
    while (i > 0) {
        if (i % 2 !== 0) {
            console.log(i);
        }
        i--;
    }
}
state4();
//#endregion
//#region 문제5번함수
function state5(){
    var result = 0;
    for (var i = 0; i < 10; i++) {
    result += i;
    }
    console.log(result);
};
state5();

//#endregion

//#region 문제6번함수
function state6() {
    var result = 0;
    for(var i = 1; i<20; i++){
        if(i%2 !== 0 && i%3 !== 0)
        {
            result += i;
        }
    }
    console.log(result);
};
state6();
//#endregion

//#region 문제7번함수
function state7() {
    var result = 0;
    for (var i = 1; i < 21; i++) {
        if (i % 2 === 0 || i % 3 === 0) {
            result += i;
        }
    }
    console.log(result);
};
state7();
//#endregion

//#region 문제8번함수
function state8() {
    for(var i =1; i<7;i++){
        for(var j = 1; j<7; j++){
            if(i+j === 6){
                console.log('[' + i +','+ j+ ']');
            }
        }
    }
};
state8();
//#endregion

//#region 문제9번함수
function state9() {
    var result = '';
    var line = 5;
    for(var i = 0 ; i < line; i++)
    {   
        result += '*';
        console.log(result);
    }
};
state9();
//#endregion

//#region 문제10번함수
function state10() 
{
    var result = '';
    var result2 = '';
    var line_one = 3;
    var line_two = 5;
    for (var i = 0; i < line_one; i++) 
    {
        result += '*'
        console.log(result);
    }
    for (var j = 0; j < line_two; j++ )
    {
        result2 += '*'
        console.log(result2);
    }
};
state10();
//#endregion

// 이밑으로는 다른방법으로 접근 

//#region 문제11번함수
function state11() {
    var result = '';
    var result2 = '';
    var line = 8;
    for(var i = 0; i< line; i++ )
    {
        if(i<line-5)
        {
            result += '*';
            console.log(result);
        }
        else if (i<line)
        {
            result2 += '*';
            console.log(result2);
        }
    }
};
state11();
//#endregion

//#region 문제13번함수
function state13() {
    var result = '';
    var star = '';
    for (var i = 0; i < 5; i++) {
        for(var j=0; j<i+1 ; j++){
            star += '*';
            result += star + '\n';
            if(i<5){
                break;
            }
        }
    }
    console.log(result);
};
state13();
//#endregion
```

