## Python sorting Algorithm

1. 선택정렬 (Selection sort)

   ```python
   # 리스트의 내림차순으로 정렬 ex) [0,1,2,3,4,6,7,8,9]
   list = [9,1,6,8,4,3,2,0,7] 
   # 선택정렬은 0번 인덱스와 1번 인덱스부터 리스트의 길이만큼 반복하여 비교 연산하여 가장 낮은수를 찾아 가장 앞에 정렬 하는 방식이다. 
   
   # Selelction sort의 경우 시간복잡도는 O(n^2)이 된다.
   # python으로 Selection sorting을 구현하면 다음과 같다.
   
   # 1. sorting 함수 선언 parameter로는 리스트를 받는다.
   def selection_sort(x):
   # 2. 리스트의 길이를 변수 length에 할당
   	length = len(x)
   # 3. 먼저 parameter로 받은 리스트의 0번 인덱스를 최소값을 저장하는 변수 index_min에 할당
   # 0번인덱스의 경우 전체길이에 -1한 만큼 즉 n-1만큼 for문 실행
   	for i in range(length-1):
   	    index_min = i
   # 4. 리스트의 0번인덱스와 1번 인덱스를 비교해야 하므로(list[i] > list[i + 1]) j에 (i+1)을 할당하고 n번째 인덱스 만큼 for문을 순회해야하므로 length만큼 for문 실행
   		for j in range(i+1, length):
   # 5. 리스트의 가장 낮은 숫자의 인덱스를 비교연산하여 리스트중의 가장 낮은 숫자를 찾는다.
   			if x[index_min] > x[j]:
   				index_min = j
   # 6. 숫자를 찾는데 성공한 경우 현재 인덱스(찾은 인덱스)와 0번 인덱스를 치환
   		x[i], x[index_min] = x[index_min], x[i]
   	return x
   
   
   # 정렬 과정 
   # a. 리스트 중 최소값을 검색
   # b. 그 값을 맨 앞의 값과 교체
   # c. 나머지 리스트에서 위의 과정을 반복
   ```

   

2. 거품정렬 (Bubble sort)