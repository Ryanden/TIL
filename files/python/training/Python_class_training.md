## Python Class Algorithm

1. 일상생활에서 접할 수 있는 서로 연관되는 어떠한 것들에 대하여 3개의 클래스를 만들고, 각각에게 영향을 줄 수 있는 메서드를 만들고 사용해서 다른 인스턴스의 속성에 영향을 주는 코드를 작성해본다.

   - ex) 사람 클래스와 고양이 클래스 -> 사람이 '먹이준다' 메서드 실행 시 고양이 인스턴스를 전달, 고양이 인스턴스의 포만감을 +

   ```python
   class Human:
       def __init__(self, name):
           self.name = name
       
       def give_prey(self, target):
           target.get_satiety(self)
           print(f'{self.name}이 먹이를 줍니다')
       
   class Cat:
       def __init__(self):
           self.satiety = 0
           
       def get_satiety(self, item):
           if self.satiety >= 100:
               print('더이상 먹일 수 없습니다.')
           else:
               self.satiety += 10
               
           print(f'현재 포만감은 {self.satiety}입니다.')
   
   hite = Human('hite')
   cat = Cat()
   hite.give_prey(cat)
   # 예상 출력결과 : 더이상 먹일 수 없습니다.
   #  			   현재 포만감은 100입니다.
   #			   hite이 먹이를 줍니다.
   ```

   

2. 외부에서 조작하면 문제가 생길 수 있는 속성을 `private`하게 지정되도록 이름을 바꾸고, `property`를 만들어 본다. `setter`가 필요없는 속성은 읽기전용으로 남겨두며, 변경해야 하는 속성은 `setter`를 구현하고 제한조건을 만든다.

   - ex) 음식을 먹고 포만감을 늘리는 메서드 -> 포만감이 100이상이면 먹지 않도록

   ```python
   class Pet:
    def __init__(self, name):
        self.__satiety = 0
        self.__name = name
        
    def get_food(self):
        if self.__satiety >= 100:
            print('더이상 먹을 수 없습니다.')
        else:
            self.__satiety += 10            
        print(f'현재 {self.__name}의 포만감은 {self.__satiety}입니다.')
    
    @property
    def rate_satiety(self):
        return self.__satiety
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def change_name(self, changed_name):
        self.__name = changed_name
        print(f'펫의 이름이 {self.__name}으로 변경 되었습니다.')
        
       
   lion = Pet('lion')
   lion.get_food()
   lion.rate_satiety
   lion.change_name = 'tiger'
   # 예상 출력결과 : 더이상 먹일 수 없습니다.
   #  			   현재 lion의 포만감은 10입니다.
   #			   10
   # 펫의 이름이 tiger으로 변경 되었습니다.
   ```
