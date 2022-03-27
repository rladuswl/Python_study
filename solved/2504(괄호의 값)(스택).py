# 2504 괄호의 값

# isdigit() : 해당 문자열이 '숫자'로 이루어져 있는지 검사
# isdecimal() : 해당 문자열이 0~9까지의 수로 이루어진 것인지 검사 (int로 바로 변환할 수 있어야 함)

'''틀림 - 왜????????????????????
string = input()

stack = []
for i in string:
    if i == ')':
        s = 0
        while len(stack)!=0:
            pop = stack.pop()
            if pop == '(':
                if s == 0:
                    stack.append(2)
                else:
                    stack.append(s*2)
                break
            elif pop == '[':
                print(0)
                exit(0)
            else:
                s = s + int(pop)
        #print('3', stack)

    elif i == ']':
        s = 0
        while len(stack)!=0:
            pop = stack.pop()
            if pop == '[':
                if s == 0:
                    stack.append(3)
                else:
                    stack.append(s * 3)
                break
            elif pop == '(':
                print(0)
                exit(0)
            else:
                s = s + int(pop)
        #print('4', stack)

    else:
        stack.append(i)

result = 0
for x in stack:
    if x == '(' or x == '[':
        print(0)
        exit(0)
    else:
        result += x

print(result)
'''
