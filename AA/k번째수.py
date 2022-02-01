import sys
sys.stdin = open("input.txt", "rt")

## k번째 수
''' 내가 푼 답
T = int(input())  # 테스트 케이스가 몇 번인지

for t in range(1, T+1):
    n, s, e, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = []
    for j in range(s, e+1):
        b.append(a[j-1])
    b = sorted(b)

    for i in range(1, len(b)+1):
        if i == k:
            print("#{} {}".format(t, b[i-1]))
'''

T = int(input())  # 테스트 케이스가 몇 번인지

for t in range(1, T+1):
    n, s, e, k = map(int, input().split())

    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print('#%d %d' %(t, a[k-1]))