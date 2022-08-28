import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    str = input()
    print('>>' + str + '<<')
    stack = []

    for i in str:
        if i == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')