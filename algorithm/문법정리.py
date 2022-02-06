## for-else 문
'''
for i in range(1, 11):
    print(i)
    if i==5:  # 정상 종료가 아님 (break 됨) -> else문 실행 X
        break
else:
    print(11)
'''

'''
for i in range(1, 11):
    print(i)
    if i>15:  # 정상 종료임
        break
else:
    print(11)
'''

## 중첩 반복문
'''
for i in range(5):
    print('*i:', i, '*', sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()
'''

## 문자열과 내장함수 upper, lower
'''
msg = 'It is Time'
print(msg.upper())  # 대문자
print(msg.lower())  # 소문자
print(msg)
print()

tmp = msg.upper()
print('tmp:', tmp)
print(tmp.find('T'))  # 처음으로 T가 발견된 인덱스
print(tmp.count('T'))   # T가 몇 개?
print()

print('msg:', msg)
print(msg[:2])  # 인덱스 0, 1만 출력
print(len(msg))  # 길이
print()

for x in msg:
    if x.isupper():  # x가 대문자이면 참
        print(x, end=' ')
print()

print()

for x in msg:
    if x.isalpha():  # 알파벳만 출력
        print(x, end=' ')
print()

print()
tmp='AZ'
for x in tmp:
    print(ord(x), end=' ')  # 아스키코드 A(65)~Z(90) / a(97)~z(122)
print()

tmp=65
print(chr(tmp))  # 숫자를 아스키코드 문자로..
print()
'''


## 리스트와 내장함수(2)
'''
a = [23, 12, 36, 53, 19]
for index, value in enumerate(a):
    print(index, value)
print()

if all(60>x for x in a):  # x가 a 리스트 하나하나 접근하면서 60>x 조건문이 전부 참이 되면
    print('YES')
else:
    print('NO')

if any(15>x for x in a):  # x가 a 리스트 하나하나 접근하면서 15>x 조건문이 하나라도 참이 되면
    print('YES')
else:
    print('NO')
'''

## 2차원 리스트 생성과 접근 -> 표로 생각하기
'''
a = [[0]*3 for _ in range(3)]
print(a)
'''

## 함수 만들기
'''
def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
'''

## 람다 함수
'''
plus_two = lambda x: x+2
print(plus_two(1))
'''
# map(함수명, 자료) -> 인자 2개 가짐
'''
def plus_one(x):
    return x+1

a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))
'''