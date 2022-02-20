import sys
sys.stdin = open("input.txt", "rt")

## 이진트리순회 (깊이우선탐색) DFS -> 재귀 이용

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2+1)


if __name__ == '__main__':
    DFS(1)
