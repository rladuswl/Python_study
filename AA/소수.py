import sys
#sys.stdin = open("input.txt", "rt")

# ** 해답 보고 품 **

# 에라토스테네스 체 방법 사용 -> 소수를 걸러내기
## 소수 (에라토스테네스 체)
'''내 방법1 (에라토스테네스 체 방법 X) -> 시간초과
n = int(input())
cnt = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count+=1
    if count==2:
        cnt+=1

print(cnt)
'''

'''내 방법2 (에라토스테네스 체 방법 X) -> 시간초과
n = int(input())
list1 = [0]*n
for i in range(2, n+1):
    for j in range(1, i+1):
        if i % j == 0:
            list1[i-1]+=1

print(list1.count(2))
'''

'''해설'''
n = int(input())
li = [0]*(n+1)  # 인덱스 번호 20까지 만들려면 21개 필요
cnt = 0  # 소수의 개수
for i in range(2, n+1):
    if li[i] == 0:
        cnt+=1
        for j in range(i, n+1, i):
            li[j]+=1
print(cnt)
