import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 알파코드(DFS)


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
                if c[L:L+2] == i:
                    res[L] = i
                    dfs(L+2)


c = list(map(int, input()))
res = [0]*len(c)
cnt = 0
str_list = []
dfs(0)
print(cnt)