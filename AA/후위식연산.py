import sys
sys.stdin = open("input.txt", "rt")

## 후위식 연산
s = input()
stack = []
for x in s:
    if x.isdecimal():  # 피연산자이면 참
        stack.append(int(x))
    else:  # 연산자이면
        a = stack.pop()
        b = stack.pop()
        if x == '+':
            stack.append(b + a)
        elif x == '-':
            stack.append(b - a)
        elif x == '*':
            stack.append(b * a)
        elif x == '/':
            stack.append(b // a)

print(stack[0])