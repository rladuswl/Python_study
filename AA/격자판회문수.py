import sys
#sys.stdin = open("input.txt", "rt")

## 격자판 회문수
'''내 답안
cnt = 0
li = [list(map(int, input().split())) for _ in range(7)]
for a in range(7):
    for i in range(0, 3):
        row = []
        col = []
        orirow =[]
        oricol =[]
        for j in range(0, 5):
            orirow.append(li[a][j + i])  # 원본으로 쓸 리스트
            oricol.append(li[j + i][a])  # 원본
            row.append(li[a][j+i])  # 역순으로 만들 리스트
            col.append(li[j+i][a])  # 역순
        row.reverse()
        col.reverse()

        for k in range(5):
            if orirow[k] != row[k]:
                break
        else:
            cnt += 1

        for k in range(5):
            if oricol[k] != col[k]:
                break
        else:
            cnt += 1


print(cnt)
'''

'''모범답안'''
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        # 행
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        # 열 -> 슬라이스 이용할 수 없음
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)
