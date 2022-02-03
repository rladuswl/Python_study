# 홀수 행 - 홀수가 하얀 칸
# 짝수 행 - 짝수가 하얀 칸

chess = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    if i%2 != 0:
        for j in range(1, 8, 2):
            if chess[i][j] == 'F':
                cnt += 1
    else:
        for k in range(0, 8, 2):
            if chess[i][k] == 'F':
                cnt += 1

print(cnt)