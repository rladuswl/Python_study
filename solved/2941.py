# 백준 2941 크로아티아 알파벳

# 1. 입력받은 문자열을 2개 문자씩 읽으면서 cro 안에 있나 확인해본다.
# 2. 있으면 cnt += 1을 한다.
# 3. 마지막에 cnt*2 한 결과를 입력받은 전체 문자열의 길이에서 뺀다. 그러면 일반 알파벳의 개수가 나온다.
# 4. 크로아티아 알파벳이 3개 문자인 경우도 하나 있으므로 이건 따로 다룬다.
'''
import sys

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = sys.stdin.readline().rstrip()

i = 0
cnt2 = 0
cnt3 = 0
while i < len(str)-1:
    if str[i:i+3] == cro[2]:
        cnt3 += 1
        i += 3
    elif str[i:i+2] in cro:
        cnt2 += 1
        i += 2
    else:
        i += 1

print(cnt2 + cnt3 + (len(str) - ((cnt2 * 2)+(cnt3 * 3))))
'''

'''
import sys

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = sys.stdin.readline().rstrip()

for x in cro:
    str = str.replace(x, '.')

print(len(str))
'''