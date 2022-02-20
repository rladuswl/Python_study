import sys
sys.stdin = open("input.txt", "rt")

# 해설

## 부분집합 구하기(DFS)
def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)


if __name__ == '__main__':
    n = int(input())
    check=[0]*(n+1)  # 부분집합으로 사용 여부
    DFS(1)