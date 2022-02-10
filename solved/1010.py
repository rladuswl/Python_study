# 1010 다리 놓기
# 다이나믹 프로그래밍
# 조합론
# 해설참고

def f(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a*f(a-1)


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    result = f(m) // (f(n)*f(m-n))
    print(result)