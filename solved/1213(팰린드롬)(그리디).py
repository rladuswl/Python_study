## 백준 1213 팰린드롬 만들기

import sys
input = sys.stdin.readline

'''아스키코드로 푸는 방법
name = list(map(str, sys.stdin.readline().rstrip()))
alphabet_count = [0 for _ in range(26)]
for x in name:
    alphabet_count[ord(x)-65] += 1

odd_count = 0
ans = ''
odd_alpha = ''
for i in range(26):
    if alphabet_count[i]%2 == 1:
        odd_count += 1
        odd_alpha = chr(i+65)  # 가운데에 둘 하나
    ans += chr(i+65) * (alphabet_count[i]//2)  # 짝수는 반개씩만 담기

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(ans + odd_alpha + ans[::-1])
'''

'''Counter함수 사용'''

import sys
from collections import Counter

name = list(map(str, sys.stdin.readline().strip()))
name.sort()  # 사전순으로 정렬하기 위해 오름차순 정렬
check = Counter(name)  # 홀수의 개수를 확인하기 위해 Counter 함수 사용

odd = 0
center = ''
for i in check:
    if check[i]%2 == 1:
        odd += 1  # 홀수 개수 카운트
        center = i  # 홀수를 가운데에 두기 위해 값 넣어두기
        name.remove(i)
    if odd > 1:
        break

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    res = ''
    for i in range(0, len(name), 2):
        res = res + name[i]
    print(res + center + res[::-1])

