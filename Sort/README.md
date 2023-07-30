# Sort (정렬)) <br>
> 데이터를 특정한 기준에 따라서 순서대로 나열

1. 선택정렬(selection sort)<br>
   - 가장 작은 데이터를 선택해서 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복하는 알고리즘
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i #가장 작은 원소의 인덱스
        for j in (i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] #스와프

    print(array)
    ```
    - 파이썬의 경우 두 변수의 위치를 변경하는 작업이 쉽게 가능하다.
    ```python
    array = [3, 5]
    array[0], array[1] = array[1], array[0]

    print(array)
    ```

2. 삽입 정렬(insertion sort)<br>
   - 특정한 데이터를 적절한 위치에 삽입한다.<br>
   - 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입된다.
   - 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
   - 보통의 경우 O($N^2$), 최선의 경우 O(N)
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(1, len(array)):
        for j in rnage(i, 0, -1): #인덱스 i 부터 1까지 감소하며 반복
            if array[j] < array[j-1]: #왼쪽으로 한칸씩 이동
                array[j], array[j-1] = array[j-1], array[j]
            else: #자신보다 작은 데이터가 나오면 그 위치에서 멈춤
                break

    print(array)
    ```
3. 퀵 정렬(quick sort)
   - 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
   - 피벗(pivot) : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준
   - 책에서는 대표적 분할 방식인 호어 분할(Hoare partition)기준으로 퀵 정렬을 설명한다.
       - 리스트에서 첫 번째 데이터를 피벗으로 정한다.
   - 평균 시간 복잡도 O(NlogN)
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    def quick_sort(array):
        if len(array) <= 1:
            return array
        pivot = array[0] #피벗은 첫번째 원소이다(호어)
        tail = array[1:] #피벗을 제외한 리스트

        left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
        right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

        #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

    print(quick_sort(array))
    ```   
4. 계수 정렬(count sort)
   - 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
   - 데이터의 개수가 N, 데이터 중 최댓값이 K일때 최악의 경우 수행시간 O(N+K) 보장
   - 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능
   - 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    count = [0]* (max(array)+1)

    for i in rnage(len(array)):
        count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가
    
    for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
        for j in range(count[i]):
            print(i, end=' ') #띄어쓰기를 구분으로 등장한 회수만큼 인덱스 출력
    ```  

5. 파이썬의 정렬 라이브러리
   - sorted 함수는 퀵정렬과 동작방식 비슷한 병합 정렬을 기반으로 만들었다.
   - 퀵 정렬보다 느리지만 시간복잡도 O(NlogN)을 보장한다.
<br><br><br>

**코딩 테스트에서 정렬 알고리즘이 사용되는 경우**
| ||
|--------------------------|------------|
|정렬 라이브러리로 풀 수 있는 문제|단순히 정렬 기법을 알고 있는지 물어보는 문제|
|정렬 알고리즘의 원리에 대해서 물어보는 문제|선택 정렬, 삽입 정렬, 퀵 정렬등의 원리를 알고 있는지 묻는 문제|
|더 빠른 정렬이 필요한 문제|계수 정렬 등 다른 정렬 알고리즘을 이용하거나 기존 알고리즘의 구조적인 개선 거침|
