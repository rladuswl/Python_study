# 백준 4949 균형잡힌 세상

'''틀림
import sys

while True:
    s = []
    lst = sys.stdin.readline().rstrip()
    if lst == '.':  # 마지막 문장
        break
    else:
        for i in range(len(lst)):
            if lst[i] == '(' or lst[i] == '[':
                s.append(lst[i])

            elif lst[i] == ')':
                if len(s) != 0:
                    if s.pop() == '(':
                        continue
                    else:
                        print('no')
                        break

            elif lst[i] == ']':
                if len(s) != 0:
                    if s.pop() == '[':
                        continue
                    else:
                        print('no')
                        break
        else:
            if len(s) == 0:
                print('yes')
            else:
                print('no')
'''

'''성공
import sys

while True:
    s = []
    temp = True
    lst = sys.stdin.readline().rstrip()
    if lst == '.':  # 마지막 문장
        break

    for i in range(len(lst)):
        if lst[i] == '(' or lst[i] == '[':
            s.append(lst[i])

        elif lst[i] == ')':
            if not s or s[-1] == '[':
                temp = False
                break
            elif s[-1] == '(':
                s.pop()

        elif lst[i] == ']':
            if not s or s[-1] == '(':
                temp = False
                break
            elif s[-1] == '[':
                s.pop()

    if temp == True and not s:  # 비워져있으면
        print('yes')
    else:
        print('no')
'''