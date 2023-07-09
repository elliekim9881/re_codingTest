#실전문제2 왕실의 나이트
#수평으로 두칸 이동할 뒤 수직으로 한칸
#수직으로 두칸 이동한 뒤 수평으로 한칸 

step  = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

now_place = input()

row = int(now_place[1])
col = int(ord(now_place[0])) - int(ord('a')) + 1

cnt = 0
for i in step: #step 리스트속 이동 가능고자하는 위치 확인
    next_row = row + i[0]
    next_col = col + i[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8: #해당 위치로 이동이 가능하다면 cnt +1
        cnt += 1

print(cnt)