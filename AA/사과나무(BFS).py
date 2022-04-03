import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

'''BFS로 풀기'''


''' BFS 방법이 아님

# n의 중간 부분을 구한다. -> n//2
# s, e를 정해서 s~e 사이의 값을 더하면 그것이 수확한 사과 개수가 된다.
# s는 n//2 부터 시작하여 줄어들고, e는 n//2부터 시작하여 늘어난다.
# 한 줄을 모두 수확하는 라인을 기준으로 그 후부터는 s는 늘어나고 e는 줄어든다.
# 한 줄을 모두 수확하는 라인은 x라고 한다. x = n//2

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

s = n//2
e = n//2
result = sum(lst[0][s:e+1])

for x in range(1, n):
    if x <= n//2:
        s -= 1
        e += 1
        result += sum(lst[x][s:e+1])
    else:
        s += 1
        e -= 1
        result += sum(lst[x][s:e+1])

print(result)
'''