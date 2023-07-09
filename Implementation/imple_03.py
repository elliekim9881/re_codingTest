#실전문제03 게임개발
#왼쪽방향부터 차례대로 갈곳을 정함
#캐릭터의 바로 왼쬭방향에 아직 가보지 않은 칸 존재, 왼쪽방향 회전 + 왼쪽방향 전진
#가보지 않은 칸 x, 회전만 수행 + step1
#네 방향 모두 이미 가본칸 or 바다, 바라보는 방향 유지하고 한칸 뒤로이동 + step1

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

n,m = map(int,input().split()) #초기값
d = [[0] * m for _ in range(n)] #지도 0으로초기화

x,y,direction = map(int,input().split()) #캐릭터 위치
d[x][y] = 1 #입력받은 위치 방문했음

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx=[-1,0,1,0] #북 동 남 서
dy=[0,1,0,-1] #0  1  2  3



cnt = 1
turn_t = 0
while True:
    turn_left() #step1
    nx = x+dx[direction]
    ny = y+dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:  #가보지 않은 칸인 경우 이동
        d[nx][ny] = 1
        x, y  = nx, ny
        cnt += 1
        turn_t = 0
        continue
    else:       #회전후 가보지 않은 칸 x, 바다
        turn_t += 1
    if turn_t ==4: #네방향 모두 못감
        nx = x -dx[direction]
        ny = y -dy[direction]   
        if array[nx][ny] == 0: #뒤로 이동
            x,y = nx,ny
        else: #뒤가 바다
            break
        turn_t = 0
print(cnt)


