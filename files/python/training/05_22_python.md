### python 문제

```python
# 1. 매개변수로 문자열을 받고, 해당 문자열이 red면 apple을, yellow면 banana를, green이면 melon을, 어떤 경우도 아닐 경우 I don't know를 리턴하는 함수를 정의하고, 사용하여 result변수에 결과를 할당하고 print해본다.

fruit_dict = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'melon'
}

def what_fruit2(color):
    return fruit_dict.get(color,"I don't know")
    
what_fruit2('white')


# 2. 1번에서 작성한 함수에 docstring을 작성하여 함수에 대한 설명을 달아보고, help(함수명)으로 해당 설명을 출력해본다.

def my_func2(string):
        'docstring'
        result = ''
        if string == 'red':
            result = 'apple'
        elif string == 'yellow':
            result = 'banana'
        elif string == 'green':
            result = 'melon'
        else:
            result = "I don't know"
        print(result)
help(my_func2)

# 3. 한 개 또는 두 개의 숫자 인자를 전달받아, 하나가 오면 제곱, 두개를 받으면 두 수의 곱을 반환해주는 함수를 정의하고 사용해본다.
def square_or_multi_positional_args(*args):
    args_length = len(args)
    if not (args_length == 1 or args_length == 2):
        return ValueError('숫자는 1 or 2개만 입력가능')
    elif args_length == 2:
        return args[0] * args[1]
    return args[0] ** 2

square_or_multi_positional_args(1,4,2)

def square_or_multi_default_parameter(x, y = None):
    return x * y if y else x ** 2 

square_or_multi_default_parameter(2,4)
    


# 4. 두 개의 숫자를 인자로 받아 합과 차를 튜플을 이용해 동시에 반환하는 함수를 정의하고 사용해본다.

def sum_and_sub(num1, num2):
         return num1 + num2, num1 - num2

sum_and_sub(3,4)
(7, -1)
    
# 5. 위치인자 묶음을 매개변수로 가지며, 위치인자가 몇 개 전달되었는지를 print하고 개수를 리턴해주는 함수를 정의하고 사용해본다.
def get_args_count(*args):
         print(len(args))

get_args_count(5,4,3)
# 6.람다함수와 리스트 컴프리헨션을 사용해 한 줄로 구구단의 결과를 갖는 리스트를 생성해본다.
[(lambda a, b : f'{a} x {b} = {a * b}')(x,y) for x in range(2,10) for y in range(1,10)]
```

