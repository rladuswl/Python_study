import sys
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())
    a = 0

    if b == n == 0:
        break
    else:
        while pow(a, n) < b:
            a+=1

        if abs(b-pow(a-1, n)) > abs(b-pow(a, n)):
            print(a)
        else:
            print(a-1)