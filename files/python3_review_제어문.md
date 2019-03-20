## Python3 Review

### Python3 Basic

- 제어문

  - 기본적으로 코드는 위에서 아래로 해석하면서 실행하게 된다. 제어문은 코드 실행 흐름을 제어 할 수 있는 역할을 한다.

    ```python
    # 제어문은 if, for, while이 있는데 각각 사용하는 방식에 따라 코드를 반복 실행하는 역할을 한다.
    # 먼저 if 문은 bool 자료형만 사용 할 수 있다.
    
    language = 'python'
    if (language == 'python'):
        print('python')
    else:
        print('another language')
    
    # 특정한 값을 받아서 language를 비교하고 참이면 if문을 실행하고 거짓이면 else문을 실행한다.
    
    # for문은 특정한 조건을 지정된 횟수 만큼 반복 시킬 때 사용한다.
    for num in range(5):
        print(num)
    # 0~5 까지 0, 1, 2, 3, 4, 5를 출력하게되는 반복문이다. 기존 코드는 한 번만 실행 했던거와 달리 for 반복문은 지정된 횟수만큼 코드를 반복 실행하게 된다.
    
    # while문은 특정 조건을 만족 할때까지 무한으로 반복하는 제어문이다.
    num = 0
    while(num < 5):
        num = num + 1
    
    # while문은 특정 횟수가 정해져 있지 않기 때문에 조건을 만족하는한 무한반복 하여 실행한다. num은 0으로 시작하여 5보다 커질때까지 while문을 실행하고 num이 5이상이 되는 시점에서 반복을 중지한다.
    
    ```

    
