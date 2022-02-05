'''
n = int(input())
li = [0] * n

seat = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if seat[i] in li:
        cnt += 1
    else:
        li[i] = seat[i]

print(cnt)
'''

'''
n = int(input())
seat = list(map(int, input().split()))

print(n - len(set(seat)))
'''