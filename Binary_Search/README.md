# Binary Search (이진탐색)) <br>
> 반으로 쪼개면서 탐색하기

1. 순차 탐색(Sequential Search)<br>
   - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
   - 데이터의 개수가 N개 일때 최대 N번의 비교연산 필요
     -  : 시간복잡도 O(N)
    ```python
    def sequential_search(n, target, array):
        for i in range(n):  #원소를 하나씩 확인
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
            if array[i] == target:  
                return i + 1    #현재위치 반환

    input_data = input().split()
    n = int(input_data[0])  # 원소의 개수
    target = input_data[1]  #찾고자 하는 문자열

    array = input().split()

    print(sequential_search(n, target, array))
    ```

2. 이진 탐색(Binary search)<br>
   - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
     - 변수 3개 사용 : 시작점, 끝점, 중간점
   - 한번 확일할 때마다 확인하는 원소의 개수가 절반으로 줄어든다 
     - : 시간복잡도 O($log$N)
  
    ```python
    #재귀적으로 구현
    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return binary_search(array, target, start, mid-1)
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            return binary_search(array, target, mid+1, end)
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    #이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0 , n-1)
    if result == None:
        print("원소가 존재하지 않습니다")
    else:
        print(result+1)
    ```

    ```python
    #반복문으로 구현
    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start+end) // 2
            #찾은 경우 중간점 인덱스 반환
            if array[mid] == target:
                return mid
            #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            elif array[mid] > target:
                end  = mid - 1
            # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else:
                start = mid + 1

    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    #이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0 , n-1)
    if result == None:
        print("원소가 존재하지 않습니다")
    else:
        print(result+1)
    ```   
3. 빠르게 입력받기
```python
import sys
input_data = sys.stdin.readline().rstrip()
```
- sys 라이브러리 사용할 때 한 줄 입력받고 난 후 rstrip() 함수를 호출해야한다. (엔터가 줄 바꿈 기호로 입력되기 때문)
<br><br><br>
