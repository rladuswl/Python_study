import sys
sys.stdin = open("input.txt", "rt")

## 자릿수의 합
'''내 답안
def digit_sum(x):
    sum = 0
    x_str = str(x)
    for i in range(len(x_str)):  # for i in str(x)로 쓸 수 있음 -> i가 자릿 수 하나하나 접근
        sum += int(x_str[i])
    return sum

n = int(input())
list1 = list(map(int, input().split()))
max = 0
for i in range(n):
    if digit_sum(list1[i]) > max:
        max = digit_sum(list1[i])
        a = i

print(list1[a])
'''

'''해답
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(x)
'''
