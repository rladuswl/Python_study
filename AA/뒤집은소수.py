import sys
sys.stdin = open("input.txt", "rt")

# ** 해답 참고 **

# 문자열은 불변
## 뒤집은 소수
def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10+t
        x = x//10
    return res

def isPrime(x):
    cnt = 0
    if x == 1:
        return False

    '''해설'''
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:  # 나눠지는 i가 없으면 = if문 들어가지 않고 for문이 정상종료 되면
        return True

    '''내가 푼 부분
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    '''

    if cnt == 2:
        return True
    else:
        return False

n = int(input())
list1 = list(map(int, input().split()))
for i in list1:
    a = reverse(i)
    if isPrime(a) == True:
        print(a, end=' ')