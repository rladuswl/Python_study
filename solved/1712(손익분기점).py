import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 수입과 비용이 같아지는 경우 : a+(b*n) = c*n
# n = a/(c-b)
# 최초 이익이 발생할 때는 n+1

if (b>=c):
    print(-1)
else:
    print((a//(c-b))+1)