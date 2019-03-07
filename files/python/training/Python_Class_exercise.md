## Python Class Excercise

```python
class Library:
    
    def __init__(self,name):
        # name = 도서관이름 , book_list = 책목록
        self.name = name
        self.book_list = ['요리','스포츠','만화','전문서적','자기계발서']
    def add_book(self, new_book):
        find_index = 0
        for book in self.book_list:
            if book != new_book:
                self.book_list.append(new_book)
                break
            else:
                find_index += 1
        if find_index == len(target.book_list):
            print('추가하려는 책 "{new_Book}"은 이미 리스트에 존재합니다.')
    def remove_book(self, book_name):
        find_index = 0
       	prev_len = len(self.book_list)
        for book in self.book_list:
            if book == book_name:
                self.book_list.remove(book_name)
                break
            else:
                find_index += 1
        if find_index == prev_len:
            print('요청한 책 "{new_Book}"은 존재하지 않는 책입니다.')
        
    @property
    def info(self):
        return f'현재 {self.name}도서관에서 대여가능한 책의 목록은{self.book_list}입니다.'
    
    def show_book_list(self):
        print(self.info)

class Book:
    def __init__(self, book_name):
        self.book_name = book_name
        
        # target은 검색 대상
    def status(self, target, book_name):
        find_index = 0
        for book in target.book_list:
            if book == book_name:
                print(f'현재 "{book_name}"책은 "{target.name}"이 소유하고 있습니다.')
                break
            else:
                find_index += 1
        if find_index == len(target.book_list):
            print(f'"{target.name}"은 "{book_name}"책을 소유하고있지 않습니다. ')

class User:
    def __init__(self, name):
        self.name = name
        self.book_list = []
        # target = 대상이 될 도서관 인스턴스
        # book_name = 대상이 될 책 이름
    def borrow_book(self, target, book_name):
        # 대상이 된 도서관에 요청한 책이 있는지 확인 있을 경우 대여목록에 추가
        find_index = 0
        for book in target.book_list:
            if book == book_name:
                target.remove_book(book_name)
                self.book_list.append(book_name)
                print(f'"{target.name}"도서관에서 "{book_name}"책을 대여했습니다.')
                break
            else:
                find_index += 1
        if find_index == len(target.book_list):
            print(f'요청한 책({book_name})은 "{target.name}"도서관에 없습니다.')
        
    def return_book(self, target, book_name):
        # 대상이 된 도서관에 자신이 대여한 책을 반납
        find_index = 0
        prev_len = len(self.book_list)
        for book in self.book_list:
            if book == book_name:
                target.book_list.append(book_name)
                self.book_list.remove(book_name)
                print(f'"{target.name}"도서관에 "{book_name}"책을 반납했습니다.')
                break
            else:
                find_index += 1
        if find_index == prev_len:
            print(f'"{self.name}"은 반납하려는 책({book_name})을 가지고 있지 않습니다.')
        
    @property
    def info(self):
        if len(self.book_list):
            return f'현재 "{self.name}"님이 대여하고 있는 책목록은 {self.book_list}입니다.'
        else:
            return f'현재 {self.name}님은 책을 대여하고 있지 않습니다.'
    def show_book_list(self):
        print(self.info)
        
```


```python
lib = Library('성수')
```


```python
lib.info
```




    "현재 성수도서관에서 대여가능한 책의 목록은['요리', '스포츠', '만화', '전문서적', '자기계발서']입니다."




```python
rec = User('rec')
```


```python
rec.show_book_list()
```

    현재 rec님은 책을 대여하고 있지 않습니다.



```python
rec.borrow_book(lib,'요리')
```

    "성수"도서관에서 "요리"책을 대여했습니다.



```python
rec.show_book_list()
```

    현재 "rec"님이 대여하고 있는 책목록은 ['요리']입니다.



```python
rec.borrow_book(lib,'만화')
```

    "성수"도서관에서 "만화"책을 대여했습니다.



```python
rec.borrow_book(lib,'만화')
```

    요청한 책(만화)은 "성수"도서관에 없습니다.



```python
rec.show_book_list()
```

    현재 "rec"님이 대여하고 있는 책목록은 ['요리', '만화']입니다.



```python
lib.show_book_list()
```

    현재 성수도서관에서 대여가능한 책의 목록은['스포츠', '전문서적', '자기계발서']입니다.



```python
sport = Book('만화')
```


```python
sport.status(lib,'만화')
```

    "성수"은 "만화"책을 소유하고있지 않습니다. 



```python
sport.status(rec,'만화')
```

    현재 "만화"책은 "rec"이 소유하고 있습니다.



```python
rec.return_book(lib,'a')
```

    "rec"은 반납하려는 책(a)을 가지고 있지 않습니다.



```python
rec.return_book(lib,'요리')
```

    "성수"도서관에 "요리"책을 반납했습니다.


