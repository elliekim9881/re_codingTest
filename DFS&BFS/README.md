# DFS / BFS
> 그래프를 탐색하기 위한 대표적인 두가지 알고리즘

- push : 데이터 삽입
- pop  : 데이터 삭제
- overflow : 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
- underflow : 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행 시 발생
## Stack
> FILO(First In Last Out), LIFO(Last In First Out)

append() 매서드와 pop()매서드 사용 시 별도의 라이브러리 사용 없이 동작.

## Queue
> FIFO(First In First Out)

collections 모듈의 deque 자료구조 활용 시 큐 구현 가능.<br>
list(queue) : deque 객체를 리스트 자료형으로 변경 가능

## 재귀함수
> 자기 자신을 다시 호출하는 함수
```python
def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()

recursive_function()    # 무한대로 재귀호출을 진행할 수는 없다.
```
> 재귀함수 사용 시 재귀함수가 언제 끝날지, 종료조건을 명시해야한다.
```python
def recursive_function(i):
    if i == 100:        #100번째 출력 시 종료되도록 종료조건 명시
        return
    print(i, '번째 재귀함수', i+1, '번째 재귀함수를 호출')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function() 
```
재귀 함수의 수행은 스택 자료구조를 이용한다. 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료된다. <br>따라서 스택 자료구조를 활용해야하는 상당수 알고리즘은 재귀함수를 이용하여 간편하게 구현될 수 있다.

## DFS(Depth First Search)
> 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.<br>
> 그래프는 Node(Vertex), Edge로 표현한다.<br>
> 두 Node가 Edge로 연결되어 있다면 '두 노드는 인접하다(Adjacent)'고 표현

- 인접 행렬 (Adjacent Matrix) : 2차원 배열로 그래프의 연결관계를 표현
- 인접 리스트 (Adjacent List) : 리스트로 그래프의 연결 관계를 표현
- 동작 과정
 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
 2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 그 인접노드를 스택에 넣고 방문처리.<br>
   방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
 3. 2번의 과정을 더 이상 수행 할 수 없을 때까지 반복한다.

## BFS(Breadth First Search)
> 너비 우선 탐색.<br>
> 가까운 노드부터 탐색하는 알고리즘
- 동작 과정
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

