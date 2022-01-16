import sys
sys.stdin = open("input.txt", "rt")

## 정다면체
'''내 답안
n, m = map(int, input().split())

list1 = []
for i in range(1, n+1):
    for j in range(1, m+1):
        list1.append(i+j)

max = 0
list2 = []
for k in range(2, (n+m)+1):
    if list1.count(k) > max:
        max = list1.count(k)

for z in range(2, (n+m)+1):
    if list1.count(z) == max:
        list2.append(z)

list2.sort()
for i in list2:
    print(i, end=' ')
'''

'''해답
n, m = map(int, input().split())

list2 = [0]*(n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        list2[i+j]+=1

max = 0
for j in range(n+m+1):
    if list2[j] > max:
        max = list2[j]

for k in range(n+m+1):
    if list2[k] == max:
        print(k, end=' ')
'''