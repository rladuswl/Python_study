## 백준 1417 국회의원 선거
# 그리디
''' 틀림
import sys
input = sys.stdin.readline

n = int(input())  # 후보의 수 n명

lst = [0]
for _ in range(n):
    lst.append(int(input()))
print(lst)

cnt = 0  # 매수해야 하는 사람
if lst.count(max(lst)) == 1 and max(lst) == lst[1]:
    print(0)
else:
    while True:
        for i in range(2, n+1):
            if lst[i] >= lst[1]:
                lst[i] -= 1
                lst[1] += 1
                cnt += 1
        if lst.count(max(lst)) == 1 and max(lst) == lst[1]:
            print(cnt)
            break
'''

import sys
input = sys.stdin.readline

n = int(input())  # 후보의 수 n명

lst = [0]
for _ in range(n):
    lst.append(int(input()))

cnt = 0  # 매수해야 하는 사람
if lst.count(max(lst)) == 1 and max(lst) == lst[1]:  # 다솜이의 표 수가 max이고, max는 다솜이 뿐 일 때!
    print(0)
else:
    while True:
        find_max = 0
        find_max_index = 0
        for i in range(2, n+1):  # 2번부터 n번까지 표 수 중 max 찾기
            if lst[i] > find_max:
                find_max = lst[i]
                find_max_index = i

        if find_max >= lst[1]:  # 찾은 max와 다솜이 비교하기
            lst[find_max_index] -= 1
            lst[1] += 1
            cnt += 1

        if lst.count(max(lst)) == 1 and max(lst) == lst[1]:  # 비교 후, 다솜이가 유일한 max이면 출력
            print(cnt)
            break