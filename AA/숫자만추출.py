import sys
sys.stdin = open("input.txt", "rt")

# 해설 참고하여 풀음
# <숫자 판별 함수> 주어진 문자열이 숫자로 되어있는지 검사하는 함수
# isdigit() : 해당 문자열이 '숫자' 로 이루어져 있는지
# isdecimal() : 0~9까지의 숫자만 찾기 = 주어진 문자열을 int형으로 반환 가능해야한다.
# isnumeric() : 숫자값 표현에 해당하는 문자열까지 인정, 수로 볼 수 있는 것. 제곱근, 분수, 거듭제곱 등

## 숫자만 추출
'''내 답안
s = input()
string = ''
for x in s:
    if x.isdecimal():
        string = string + x
intstr = int(string)
print(intstr)

count = 0
for i in range(1, intstr+1):
    if intstr % i == 0:
        count += 1

print(count)
'''

'''모범답안'''
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10+int(x)  # 최고 첫 자리의 0을 무시할 수 있음
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)