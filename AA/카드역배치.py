import sys
#sys.stdin = open("input.txt", "rt")

# 카드 역배치
'''내 답안
card = []
for i in range(0, 21):
    card.append(i)

for i in range(10):
    list1 = []
    z = 0
    ai, bi = map(int, input().split())
    for j in range(ai, bi+1):
        list1.append(card[j])
    list1.reverse()

    for k in range(ai, bi+1):
        card[k] = list1[z]
        z+=1

for i in range(1, len(card)):
    print(card[i], end=' ')
'''

# 바꿔주는 횟수(e-s+1)//2 -> 짝수 홀수 모두 성립
# 2~7 이면 (7-2+1)//2 = 3 이다. ( 2<->7, 3<->6, 4<->5 총 3번 )
# swap 방법 새로 알게 됨
'''모범답안
a = list(range(21))
for _ in range(10):  # 언더바 = 변수 없이 반복
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for x in a:
    print(x, end=' ')
'''