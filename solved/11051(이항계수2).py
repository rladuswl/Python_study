n, k = map(int, input().split())

a = []
for i in range(n+1):
    a.append([1]*(i+1))

for i in range(2, n+1):
    for j in range(1, i):
        a[i][j] = (a[i-1][j-1] + a[i-1][j]) % 10007

print(a[n][k])