# 간단하지만 귀찮은 영상처리 과제가 주어졌다. 과제의 명세는 다음과 같다.
# 세로 길이가 N이고 가로 길이가 M인 화면은 총 N × M개의 픽셀로 구성되어 있고
# (i, j)에 있는 픽셀은 $R_{i,j}$ (Red), $G_{i,j}$ (Green), $B_{i,j}$ (Blue) 3가지 색상의 의미를 담고 있다. 각 색상은 0이상 255이하인 값으로 표현 가능하다.
# 모든 픽셀에서 세 가지 색상을 평균내어 경계값 T보다 크거나 같으면 픽셀의 값을 255로, 작으면 0으로 바꿔서 새로운 화면으로 저장한다.
# 새로 만들어진 화면에서 값이 255인 픽셀은 물체로 인식한다. 값이 255인 픽셀들이 상하좌우로 인접해있다면 이 픽셀들은 같은 물체로 인식된다.
# 화면에서 물체가 총 몇 개 있는지 구하는 프로그램을 작성하시오.
# 화면의 세로 N, 가로 M 값이 공백으로 구분되어 주어진다.
# 두 번째 줄부터 N + 1줄까지 i번째 가로를 구성하고 있는 픽셀의 R_{i,j}, G_{i,j}, B_{i,j}의 값이 공백으로 구분되어 총 M개 주어진다.
# 마지막 줄에는 경계값 T가 주어진다.
# 화면의 세로 길이와 가로 길이를 입력받는다.
# from collections import deque
N, M = map(int, input().split())

graph = []
cnt = 0

for _ in range(N):
    pix = list(map(int, input().split()))
    row = []
    for i in range(M):
        k = pix[i*3] + pix[i*3+1] + pix[i*3+2]
        row.append(k/3)
    graph.append(row)

T = int(input())

def dfs(row, col, T):
    global count
    if row >= N or row < 0 or col >= M or col < 0:
        return 0
    elif graph[row][col] < T:
        return 0
    else:
        graph[row][col] = -1
        dfs(row+1, col, T)
        dfs(row-1, col, T)
        dfs(row, col+1, T)
        dfs(row, col-1, T)
        return 1
    return 0

for row in range(N):
    for col in range(M):
        if dfs(row, col, T) >= T:
            cnt += dfs(row, col, T)

print(cnt)

#runtime error?