# 2504 괄호의 값

# 0. ex) (()[[]])([])
# 1. for문을 돌면서 '()'는 '2', '[]'는 '3'으로 바꾼다 (replace함수)
# 2. (2[3])(3) 을 스택에 넣는다
# 3. ) 또는 ] 이 나오면 스택에서 반대 짝을 만날 때까지 pop을 한다

# isdigit() : 해당 문자열이 '숫자'로 이루어져 있는지 검사
# isdecimal() : 해당 문자열이 0~9까지의 수로 이루어진 것인지 검사 (int로 바로 변환할 수 있어야 함)

'''틀림'''
string = input()

#string = string.replace('()', '2')
#string = string.replace('[]', '3')

stack = []
for i in string:
    if i == '(' or i == '[':
        stack.append(i)
        #print('1', stack)

    #elif i.isdigit():
        #stack.append(i)
        #print('2', stack)

    elif i == ')':
        s = 0
        while stack:
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
        while stack:
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

result = 0
for x in stack:
    if x == '(' or x == '[':
        print(0)
        exit(0)
    result += int(x)

print(result)
