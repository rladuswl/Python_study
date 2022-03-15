## 백준 1105 팔
# 그리디, 수학

'''시간초과
import sys
input = sys.stdin.readline

L, R = map(int, input().split())

m = 2147000000  # 최소값
for i in range(L, R+1):
    s = str(i)
    if s.count('8') < m:
        m = s.count('8')
print(m)
'''

'''시간초과
import sys
input = sys.stdin.readline

L, R = map(int, input().split())

L_cnt = 0  # L의 8개수 (인덱스 0에서부터 연속으로 나오는 8개수)
for i in range(len(str(L))):
    if str(L)[i] != '8':
        break
    L_cnt += 1

R_cnt = 0  # R의 8개수 (인덱스 0에서부터 연속으로 나오는 8개수)
for i in range(len(str(R))):
    if str(R)[i] != '8':
        break
    R_cnt += 1

m = min(L_cnt, R_cnt)
L_str = str(L)[m:]
R_str = str(R)[m:]

if L_str == '' or R_str == '':
    print(m)
else:
    minus = int(L_str) - int(R_str)
    minus = abs(minus)

    minus_min = 2147000000
    for i in range(minus):
        s = str(i)
        if s.count('8') < minus_min:
            minus_min = s.count('8')

    print(minus_min + m)
'''

'''정답'''
import sys
input = sys.stdin.readline

L, R = map(int, input().split())

# 자릿수가 다르면 8이 들어가는 최소 횟수는 0 (8이 없는 숫자를 꼭 지나치게 되기 때문)
# 앞자리 다르면 8이 들어가는 최소 횟수는 0 (8이 없는 숫자를 꼭 지나치게 되기 때문)

if len(str(L)) != len(str(R)):
    print(0)
elif str(L)[0] != str(R)[0]:
    print(0)
else:
    cnt = 0
    if str(L)[0] == '8':  # 앞자리수가 8이 아닌 다른 숫자로 같을 수도 있기 때문에 8인지 확인
        cnt += 1
    for i in range(1, len(str(L))):
        if str(L)[i] != str(R)[i]:
            break
        elif str(L)[i] == '8':  # elif로 8인지 한 번 더 검사해야함
            cnt += 1
    print(cnt)