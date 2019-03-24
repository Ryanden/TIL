## Python3 Review

### Python3 Basic

- 클래스

  - 클래스는 다양한 인스턴스를 만들어 낼 수 있는 메서드(함수) 및 멤버변수(클래스 내 지역변수)를 사용 할 수 있게 해주는 특징이 있다

    ```python
    class Item:
        
        def __init__(self, name):
            self.name = name
        
        def show_info(self):
            print(self.name)
            
    
    class Weapon(Item):
        def __init__(self, name, price):
            self.name = name
            self.price = price
        
        def show_info(self):
            print(f'이름 : {self.name} / 가격 : {self.price}')
            
            
    # class를 사용하면 인스턴스를 만들 수 있고 클래스로 인스턴스를 만들면 내부에 있는 모든 멤버변수 및 메서드를 사용 가능하다. Weapon클래스는 Item이라는 클래스를 상속받아 새로운 멤버변수인 price를 만들고 기존 show_info를 오버라이딩 해서 가격을 같이 출력하는 클래스를 새로 만들었다. 
    
    my_class = Weapon('검', 100)
    my_class.show_info()
    
    '이름 : 검 / 가격 : 100'
    ```

    

