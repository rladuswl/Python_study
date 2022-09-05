import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = []
for i in range(1, k+1):
    origin = n*i
    new = ''
    for j in range(len(str(origin))-1, -1, -1):
        new += str(origin)[j]
    result.append(int(new))

print(max(result))