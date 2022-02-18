# 백준 1110 더하기 사이클

# 1. n 문자열로 입력받기
# 2. 인덱스로 나눠서 int로 형 변환 후 연산 하기
# 3. 문자열 다시 붙이기
# 4. 새로운 수를 구할 때마다 cnt += 1을 하고, 새로운 수가 n과 같아지면 반복문 나오기

import sys
n = sys.stdin.readline().rstrip()

if int(n) < 10:
    n = '0' + n

nn = n

sum = 0
cnt = 0
new = -1
while new != n:
    sum = int(nn[0]) + int(nn[1])
    sum = str(sum)
    new = nn[1] + sum[-1]
    nn = new
    cnt += 1

print(cnt)