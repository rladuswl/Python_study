import sys
sys.stdin = open("input.txt", "rt")

# 시간초과 잡기
# 지역변수와 전역변수 개념

## 바둑이 승차(DFS)

# 부분집합 개념

'''시간초과
def DFS(i, sum):
    if i > len(dog)-1:
        m.append(sum)
        return
    else:
        DFS(i+1, sum+dog[i])
        DFS(i+1, sum)




if __name__ == '__main__':
    c, n = map(int, sys.stdin.readline().split())
    dog = list(int(sys.stdin.readline()) for _ in range(n))
    i = 0
    sum = 0
    m = []
    DFS(i, sum)
    while True:
        if max(m) > c:
            m[m.index(max(m))] = 0
        else:
            print(max(m))
            break
'''

'''시간초과
def DFS(i, sum, mm):
    if i == len(dog):
        if sum < c:
            mm.append(sum)
        return
    else:
        DFS(i+1, sum+dog[i], mm)
        DFS(i+1, sum, mm)




if __name__ == '__main__':
    c, n = map(int, sys.stdin.readline().split())
    dog = list(int(sys.stdin.readline()) for _ in range(n))
    i = 0
    sum = 0
    mm = []
    m = []
    DFS(i, sum, mm)
    print(max(mm))
'''

'''해설'''

from collections import deque

def DFS(L, sum, tsum):  # L은 인덱스, sum은 부분집합의 합
    global result

    if sum + (total - tsum) < result:
        return

    if sum > c:
        return

    if L == n:
        if sum > result:
            result = sum
        return
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__ == '__main__':
    c, n = map(int, sys.stdin.readline().split())
    a = [0]*n
    result = -2147000000  # 가장 작은 값으로 초기화 (최대값 구하기 위해)
    for i in range(n):
        a[i] = int(sys.stdin.readline())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
