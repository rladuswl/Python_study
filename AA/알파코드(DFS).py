import sys
#sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

## 알파코드(DFS)

'''틀림
def dfs(L):
    global cnt
    global res
    if L == len(c):
        s = ''
        for x in res:
            s += chr(64 + x)
        str_list.append(s)
        cnt += 1
        res = [0]*len(c)
    else:
        for i in range(1, 27):
            if c[L] == i and len(str(i)) == 1:
                res[L] = i
                dfs(L+1)
            elif len(str(i)) == 2:
                two_c = ''
                if L <= 3:
                    two_c = str(c[L]) + str(c[L+1])  # 두자리 수
                    if two_c == i:
                        res[L] = i
                        dfs(L+2)


c = list(map(int, input()))
res = [0]*len(c)
cnt = 0
str_list = []
dfs(0)
for x in str_list:
    print(x)
print(cnt)
'''

def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P): # P가 하나 증가해서 왔기 때문에 0~P까지 돌게 됨
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):  # 1~26
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i>=10 and code[L] == i//10 and code[L+1] == i%10:  # i가 두자리 숫자일때
                res[P] = i
                DFS(L+2, P+1)

code = list(map(int, input()))  # 입력 리스트로 받기
n = len(code)
code.insert(n, -1)
res = [0] * (n+3)
cnt = 0
DFS(0, 0)

print(cnt)
