import sys
sys.stdin = open("input.txt", "rt")

## 스토쿠 검사
'''내 답안
list1 = [list(map(int, input().split())) for _ in range(9)]
str = 'YES'

# 행
for i in range(9):
    temp = sorted(list1[i])
    for j in range(9):
        if temp[j] == j+1:
            str = 'YES'
        else:
            str = 'NO'
            break
    if str == 'NO':
        print('NO')
        break

# 열
if str != 'NO':
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(list1[j][i])
        temp = sorted(temp)
        for k in range(9):
            if temp[k] == k+1:
                str = 'YES'
            else:
                str = 'NO'
                break
        if str == 'NO':
            print('NO')
            break

# 3x3
if str != 'NO':
    for i in range(0, 7, 3):
        temp = []
        for j in range(3):
            for k in range(3):
                temp.append(list1[j+i][k])
        temp = sorted(temp)
        for k in range(9):
            if temp[k] == k+1:
                str = 'YES'
            else:
                str = 'NO'
                break
        if str == 'NO':
            print('NO')
            break

if str != 'NO':
    for i in range(0, 7, 3):
        temp = []
        for j in range(3):
            for k in range(3):
                temp.append(list1[j+i][k+3])
        temp = sorted(temp)
        for k in range(9):
            if temp[k] == k+1:
                str = 'YES'
            else:
                str = 'NO'
                break
        if str == 'NO':
            print('NO')
            break

if str != 'NO':
    for i in range(0, 7, 3):
        temp = []
        for j in range(3):
            for k in range(3):
                temp.append(list1[j+i][k+6])
        temp = sorted(temp)
        for k in range(9):
            if temp[k] == k+1:
                str = 'YES'
            else:
                str = 'NO'
                break
        if str == 'NO':
            print('NO')
            break

if str != 'NO':
    print(str)
'''

'''모범답안'''

def check(a):
    # ch1 = 행, ch2 = 열
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False

    # 3x3 블럭
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[k+i*3][s+j*3]] = 1
            if sum(ch3) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")