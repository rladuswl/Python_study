import sys
sys.stdin = open("input.txt", "rt")

## 합이 같은 부분집합 (DFS : 아마존 인터뷰)

# 1. 트리로 만든다.
# 2. 부분집합이 되는 경우를 구한다. (재귀)
# 3. 그때의 나머지 원소들의 합과 부분집합의 합이 같은지 확인한다.
'''내 답안
def DFS(i):
    if i < len(lst):
        ch[i] = 1
        DFS(i+1)
        ch[i] = 0
        DFS(i+1)
    else:
        sum1 = 0
        sum2 = 0
        for j in range(len(ch)):
            if ch[j] == 1:
                sum1 += lst[j]
            else:
                sum2 += lst[j]
        if sum1 == sum2:
            print('YES')
            sys.exit(0)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    ch = [0 for _ in range(n)]
    i = 0
    DFS(i)
    print('N0')
'''

def DFS(L, sum):  # L은 인덱스 겸 레벨
    if sum > total//2:  # 시간복잡도 줄이기
        return
    if L == n:
        if sum == (total-sum):
            print('YES')
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])  # 부분집합으로 사용
        DFS(L+1, sum)  # 부분집합으로 사용X


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    total = sum(a)
    DFS(0, 0)
    print('NO')

