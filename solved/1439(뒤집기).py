import sys
input = sys.stdin.readline

s = input().rstrip()

if s[0] == '1':
    one_zero = 0
    zero_one = 1
else:
    one_zero = 1
    zero_one = 0

tf = True  # 전체가 같은 문자인지(True), 다른 문자인지(False)

for i in range(len(s)):
    if s[i] == s[0]:
        continue
    else:
        tf = False
        break

if tf == False:
    for i in range(len(s)-1):
        if s[i] == '0' and s[i+1] == '1':
            zero_one += 1
        elif s[i] == '1' and s[i+1] == '0':
            one_zero += 1
        else:
            continue
    print(min(zero_one, one_zero))
else:
    print(0)
