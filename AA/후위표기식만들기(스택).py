import sys
#sys.stdin = open("input.txt", "rt")

# 틀림
# 10진수 숫자인지 확인하는 함수 : isdecimal()

## 후위표기식 만들기
'''내 답안
a = input()
stack = []
result = ''
for i in range(len(a)):
    if a[i] == '+' or a[i] == '-':
        while len(stack) != 0 and (stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/'):
            result = result + stack.pop()
        stack.append(a[i])

    elif a[i] == '*' or a[i] == '/':
        while len(stack) != 0 and (stack[-1] == '*' or stack[-1] == '/'):
            result = result + stack.pop()
        stack.append(a[i])

    elif a[i] == '(' or a[i] == ')':
        if a[i] == '(':
            stack.append('(')
        elif a[i] == ')':
            m = stack.pop()
            while m != '(':
                result = result + m
                m = stack.pop()

    else:
        result = result + a[i]

if len(stack) != 0:
    for i in range(1, len(stack)+1):
        result = result + stack[-i]
print(result)
'''


'''모범답안
a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():  # 피연산자
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
'''