#단어수학

n = int(input())

words = []

for _ in range(n):
    words.append(input())

dict = {}

for word in words:
    square = len(word) -1 #맨 마지막자리 0제곱
    for i in word: 
        if i in dict:
            dict[i] += pow(10, square) #값이 있는 경우에 더해줌
        else:
            dict[i] = pow(10, square) #없다면 그대로 넣어줌
        square -= 1 #제곱근 빼줌

dict = sorted(dict.values(), reverse=True)

result = 0
tmp = 9


for i in dict: #sort 한 리스트이용, 값 계산하기
    result += i * tmp
    tmp -= 1

print(result)
