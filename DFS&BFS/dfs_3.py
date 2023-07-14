n, m = map(int, input().split())

#맵 정보 입력 , 2차원 리스트
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#dfs로 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: #현재 노드를 방문하지 않았을 경우
        graph[x][y] = 1 #방문처리
        #연결된 모든 노드 방문 , 재귀
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

#모든 노드에 음료수
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
