import sys
sys.stdin = open("input.txt", "rt")

## 재귀함수를 이용한 이진수 출력

'''내 답안
def solution(n):
    s = ''
    if n//2 != 0:
        solution(n//2)
    s = str(n%2)
    print(s, end='')

n = int(sys.stdin.readline())  # 10진수 n 입력
solution(n)
'''

def DFS(x):
    if x == 0:
        return  # 함수 종료하라는 명령어 역할
    else:
        DFS(x//2)
        print(x % 2, end='')



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    DFS(n)