import sys
sys.stdin = open("input.txt", "rt")

# 틀림, 다시풀기 맞음
# 스택
# 앞 숫자가 현재 숫자보다 작으면 지우고 앞으로 가기 (n번)
# 모범답안에서 res=''.join(map(str, stack)) 기능 익히기

## 가장 큰 수 (스택)
'''내 답안
a, b = map(int, input().split())
a = str(a)
m = len(a) - b
s = 0
ans = ''
for i in range(m):
    if s+m <= len(a):
        x = max(a[s:s+m])
        ans = ans + x

        for j in range(s, s+m):
            if a[j] == x:
                xindex = j
                break
        s = xindex + 1

    else:
        ans = ans + a[s:]
        break

ans = int(ans)
print(ans)
'''
'''다시 풀기
a, b = map(int, input().split())
li = []
a = str(a)
for i in range(len(a)):
    li.append(int(a[i]))

cnt = 0
ans = [li[0]]
for i in range(1, len(a)):
    if ans[-1] < li[i]:
        while ans != [] and ans[-1] < li[i]:
            ans.pop()
            cnt += 1
            if cnt == b:
                break
        ans.append(li[i])
    else:
        ans.append(li[i])

    if cnt >= b:
        for x in range(i+1, len(li)):
            ans.append(li[x])
        break

if cnt < b:
    for x in range(b-cnt):
        ans.pop()

for x in ans:
    print(x, end='')
'''

'''모범답안'''
num, m = map(int, input().split())
num = list(map(int, str(num)))  # 리스트화 시키는 법
stack = []
for x in num:
    while stack and m>0 and stack[-1] < x:  # stack 이 비어있으면 거짓, 아니면 참
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]  # 뒤쪽의 m개 날리기

res = ''.join(map(str, stack))
print(res)