import sys
sys.stdin = open("input.txt", "rt")

# 아스키코드 A = 65, a = 97

## 회문 문자열 검사
'''내 답안
n = int(input())
for i in range(n):
    string = input()
    for a in range(0, len(string)):
        if string[a] == string[len(string)-(a+1)]:
            ans = 'YES'
        else:
            if ord(string[a]) > ord(string[len(string)-(a+1)]):
                if ord(string[a]) == ord(string[len(string)-(a+1)])+32:
                    ans = 'YES'
                else:
                    ans = 'NO'
                    break
            elif ord(string[a]) < ord(string[len(string)-(a+1)]):
                if ord(string[a])+32 == ord(string[len(string)-(a+1)]):
                    ans = 'YES'
                else:
                    ans = 'NO'
                    break
    print('#{} {}'.format(i+1, ans))
'''

# 문자열이 들어오면 먼저 전부 대문자로 바꿔서 비교하기
# 문자 사이즈가 홀수이면 정 중앙의 문자 하나는 비교하지 않아도 됨
# 인덱스 번호를 반대로부터 세면 -1, -2, -3...
# for - else 문

'''모범답안1
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))
'''

# s[::-1] - reverse 시켜주는 코드
# 직접 비교하는 방법은 아님
'''모범답안2
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print('#%d YES' % (i + 1))
    else:
        print('#%d NO' % (i + 1))
'''