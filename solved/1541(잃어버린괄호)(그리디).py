## 백준 1541 잃어버린 괄호

import sys


'''예제3 에서 실패
string = input()

for x in string:
    if x == '-':
        s = ''
        status = False
        for j in range(string.index(x)+1, len(string)):
            if string[j] == '-':
                status = True
                break
            s += string[j]
        if status == True:
            string = string.replace(string[string.index(x) + 1:j], str(eval(s)))
        else:
            print(eval(s))
            string = string.replace(string[string.index(x)+1:j+1], str(eval(s)))
print(eval(string))
'''

'''찾아본 풀이'''

string = input().split('-')

s = 0

for i in string[0].split('+'):
    s += int(i)

for i in string[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)