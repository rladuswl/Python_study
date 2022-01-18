import sys
sys.stdin = open("input.txt", "rt")

# 난 왜이렇게 어렵게 푸는 걸까..
## 점수계산
'''내 답안
n = int(input())
list1 = list(map(int, input().split()))
list2 = [0]*n
cnt = 0
sum = 0
for i in range(n):
    if list1[i] == 0:
        list2[i] = 0
        cnt = 0
    else:
        cnt+=1
        list2[i] = cnt

for j in list2:
    sum += j
print(sum)
'''

'''모범답안
n = int(input())
list1 = list(map(int, input().split()))
cnt = 0
sum = 0
for i in list1:
    if i == 1:
        cnt+=1
        sum+=cnt
    else:
        cnt = 0
print(sum)
'''