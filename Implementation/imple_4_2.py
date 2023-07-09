#4-2 시각
n = int(input())
# 24시 60분 60초

cnt = 0

for i in range(n+1): #n시 포함해야함
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt) 

#탐색해야할 데이터의 개수가 100만개 이하일 때 완전탐색 사용