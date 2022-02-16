# 백준 2153 소수 단어
# 수학, 문자열, 정수론, 소수판정
import sys
input = sys.stdin.readline

low = 'abcdefghijklmnopqrstuvwxyz'
up = low.upper()
tot = list(low+up)

sum = 0
str = list(sys.stdin.readline().rstrip())

for x in str:
    if x in tot:
        sum += tot.index(x)+1


cnt = 0
for i in range(1, sum+1):
    if sum%i == 0:
        cnt += 1

if cnt == 2 or sum == 1:
    print('It is a prime word.')
else:
    print('It is not a prime word.')