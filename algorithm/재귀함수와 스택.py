# 재귀함수와 스택
# 재귀는 스택을 사용

import sys
sys.stdin = open("input.txt", "rt")

def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x)



if __name__ == "__main__":
    n = int(sys.stdin.readline())
    DFS(n)