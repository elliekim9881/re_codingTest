# 첫 번째 줄에 가려진 노드를 포함한 노드의 개수 
# $N$이 주어진다. 
# $(N=2^k-1;$ 
# $2 \le k \le 17;$ 
# $k$는 정수
# $)$ 

# 두 번째 줄에 
# $A_1, A_2, \cdots, A_N$이 공백으로 구분되어 주어진다. 
# $A_i$는 
# $i$번 노드에 적혀있는 수이다. 
# $(0 \le A_i \le 10^9;$ 가려진 하나의 노드에 대해서만 
# $A_i = -1)$ 
# $i \neq j$이면 
# $A_i \neq A_j$이다. 노드 번호는 루트 노드부터 시작하여, 같은 깊이 내 왼쪽에서 오른쪽으로 갈수록 증가하는 순서로 매겨진다 (아래 그림 참조).

# 세 번째 줄에 트리에 넣을 수 
# $X$가 주어진다. 
# $(0 \le X \le 10^9;$ 
# $X \neq A_i)$ 

# 입력으로 주어지는 모든 수는 정수이다.

# 첫 번째 줄에 바뀐 트리를 후위(postorder) 순회한 결과를 출력한다. (단, 왼쪽 자식 노드를 먼저 방문한다.)

N = int(input())

A = list(map(int, input().split()))

X = int(input())

A[A.index(-1)] = X
A.sort()


def postorder(node, a):
    if not a:
        print(A[node], end=' ')
        return
    postorder(node-a, a//2)
    postorder(node+a, a//2)
    print(A[node], end=' ')

postorder(N//2, (N+1)//4)


