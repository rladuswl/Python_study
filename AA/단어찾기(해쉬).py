import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 단어 찾기 (해쉬)
'''내 답안
n = int(input())
note = []
poem = []
for _ in range(n):
    note.append(input())

for _ in range(n-1):
    poem.append(input())

for i in note:
    if i not in poem:
        print(i)
'''

'''모범답안'''
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for j in range(n-1):
    word = input()
    p[word] = 0

for k, v in p.items():
    if p[k] == 1:
        print(k)
        break