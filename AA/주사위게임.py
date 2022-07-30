import sys
sys.stdin = open("input.txt", "rt")

## 주사위 게임
'''내 답안
n = int(input())
list1 = []
for i in range(n):
    a, b, c = map(int, input().split())
    m = 0
    if a == b == c:
        m = 10000+a*1000
    elif a == b and a != c:
        m = 1000+a*100
    elif b == c and b != a:
        m = 1000+b*100
    elif a == c and a != b:
        m = 1000+a*100
    else:
        maxv = max(a, b, c)
        m = maxv*100

    list1.append(m)

print(max(list1))
'''

''' 강의 해답'''
# 정렬을 먼저 시키기
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()  # tmp에 리스트 형태로 들어감
    tmp.sort  # 오름차순 정렬
    a, b, c = map(int, tmp)
    if a == b and b == c:  # 같은 눈 3개
        m = 10000+a*1000
    elif a == b or a == c:  # 같은 눈 2개
        m = 1000+a*100
    elif b == c:  # 같은 눈 2개
        m = 1000+b*100
    else:  # 모두 다른 눈
        m = c*100  # 오름차순 해서 a, b, c 중 c 가 가장 큼

    if m > res:
        res = m

print(res)