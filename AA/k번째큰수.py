import sys
# sys.stdin = open("input.txt", "rt")

## k번째 큰 수
'''내 답안
n, k = map(int, input().split())

list1 = list(map(int, input().split()))
sumlist = []
count=0
for i in range(0, n):
    j = i+1
    for j in range(j, n):
        z = j+1
        for z in range(z, n):
            sum = 0
            sum = list1[i] + list1[j] + list1[z]
            sumlist.append(sum)

sumlist.sort(reverse=True)

c = 0
for i in range(0, len(sumlist)):
    if sumlist[i] > sumlist[i+1]:
        c+=1
    if c == k:
        print(sumlist[i])
        break
'''

# 해답
n, k = map(int, input().split())

list1 = list(map(int, input().split()))
res = set()  # 중복을 제거하는 자료구조 (중복된 값이 들어와도 하나만 가짐)
for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            res.add(list1[i]+list1[j]+list1[z])
res = list(res)  # set 자료구조는 sort 기능이 없어서 리스트로 만듬
res.sort(reverse=True)
print(res[k-1])