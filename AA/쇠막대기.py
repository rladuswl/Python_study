import sys
#sys.stdin = open("input.txt", "rt")

# 틀림
# 스택

## 쇠막대기
'''내 답안
li = list(map(str, input()))
tmp = []
cnt = 0
for i in range(len(li)):
    if li[i] == '(':
        tmp.append(li[i])
        cnt += 1

    else:
        if tmp[-1] == ')':
            tmp.append(li[i])
        else:
            tmp.pop()
            cnt -= 1
            c = 0
            for x in tmp:
                if x == '(':
                    c += 1
                else:
                    c -= 1
            cnt += c

print(cnt)
'''


'''내 답안2'''
li = list(map(str, input()))
tmp = []
cnt = 0
for i in range(len(li)):
    if li[i] == '(':
        tmp.append(li[i])

    else:
        if li[i-1] == ')':
            tmp.pop()
            cnt += 1
        else:
            tmp.pop()
            cnt += tmp.count('(')

print(cnt)


'''모범답안
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
'''