#5-9 BFS
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

graph = [
    [],         #0
    [2,3,8],    #1
    [1, 7],     #2
    [1,4,5],    #3
    [3,5],      #4
    [3,4],      #5
    [7],        #6
    [2,6,8],    #7
    [1,7]       #8
]

#각 노드가 방문한 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 BFS 함수 호출

bfs(graph, 1, visited)