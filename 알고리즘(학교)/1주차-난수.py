## 1주차 2번 문제

import random

# n의 크기 : 10, 100, 1000, 10000

n = 10  # n은 10에서 시작하여 10, 100, 1000, 10000까지 계산됨

while n <= 10000:
    for i in range(n):
        A = random.sample(range(1, n+1), n)  # Random number generator 사용
    if n == 10:  # n이 10일 때 A[] 출력
        print(A)
    n *= 10