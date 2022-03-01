# 백준 2231 분해합

import sys
input = sys.stdin.readline

# 1. for문을 통해 n 까지 돌기
# 2. i 와 i의 각 자리수의 합을 구해야 한다.
# 3. i의 각 자리수의 합은 str 함수를 이용하여 list에 넣기
# 4. i + i의 각 자리수의 합이 n 이 되면 그때의 i 출력하기 (가장 작은 생성자)
# 5. for문이 끝날 때까지 n 과 같은 값이 나오지 않으면 0 출력

n = int(input())

for i in range(1, n+1):
    lst = list(map(int, str(i)))
    print(lst)

    if i+sum(lst) == n:
        print(i)
        break
else:
    print(0)