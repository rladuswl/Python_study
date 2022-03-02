import sys
input = sys.stdin.readline

## 백준 1934 최소 공배수
# gcd : 최대 공약수, lcm : 최소 공배수

t = int(input())

for _ in range(t):
    A, B = map(int, input().split())

    # 먼저 최대 공약수를 구한다.
    # 최대 공약수는 둘 중에 (작은 수)와 (큰수%작은수)의 최대 공약수와 같다.
    # 작은 수가 0이 될 때까지 반복하면 그 때의 큰 수가 최대 공약수이다.
    a, b = A, B
    while b != 0:
        a = a % b
        a, b = b, a

    gcd = a  # 최대 공약수

    # 최대 공약수를 이용하여 최소 공배수를 구한다.
    lcm = A *  B//a
    print(lcm)