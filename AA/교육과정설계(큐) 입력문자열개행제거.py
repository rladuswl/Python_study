import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 교육과정 설계 (큐)
'''내 답안 -> 시간초과
# must = input()  # 필수과목
must = sys.stdin.readline().rstrip()  # 입력 문자열 맨 뒤 개행 제거
n = int(input())  # n개의 수업설계
for n in range(n):
    lst = []
    queue = deque()  # 수업설계
    # sch = input()
    sch = sys.stdin.readline().rstrip()  # 입력 문자열 맨 뒤 개행 제거

    for i in range(len(sch)):
        queue.append([i, sch[i]])

    for i in range(len(must)):
        while len(queue) != 0:
            j = 0

            if must[i] == queue[j][1]:
                lst.append(queue.popleft())
                break
            else:
                queue.append(queue.popleft())


    lst_sort = sorted(lst)
    if lst == lst_sort:
        print('#{} YES'.format(n+1))
    else:
        print('#{} NO'.format(n+1))

    queue.clear()
'''

must = sys.stdin.readline().rstrip()  # 필수과목
n = int(input())  # n개의 수업설계
for n in range(n):
    sch = sys.stdin.readline().rstrip()
    queue = deque(must)
    for j in sch:
        if j in queue:
            q = queue.popleft()
            if q == j:  # 순서 맞음
                continue
            else:  # 순서에 어긋남
                print('#{} NO'.format(n+1))
                break
    else:
        if len(queue) == 0:
            print('#{} YES'.format(n+1))
        else:
            print('#{} NO'.format(n + 1))
