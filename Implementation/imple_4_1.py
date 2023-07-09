#4-1 상하좌우
n = int(input())
x, y = 1, 1
plan_map = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_t = ['L', 'R', 'U', 'D']

for plan in plan_map:
    for i in range(len(move_t)): #이동하고 좌표
        if plan == move_t[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: #공간을 벗어나는 경우 무시
        continue

    x,y = nx, ny

print(x,y)