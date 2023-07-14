#4 미로탈출
from collections import deque

n,m = map(int,input().split())

#2차원 리스트 맵 입력
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 방향 정의
dx = [-1,1,0,0] # 상 하 좌 우
dy = [0,0,-1,1]

#BFS구현
def bfs(x,y):
    # deque 
    queue = deque()
    queue.append((x,y))

    #queue가 빌때까지
    while queue:
        x,y = queue.popleft()

        #상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
#가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))