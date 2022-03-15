## 백준 1758 알바생 강호

# 그리디, 정렬

# 1. 팁이 높은 사람은 마이너스가 적게 되어야 하므로, 순서가 앞으로 와야 한다.
# 2. 내림차순으로 순서를 바꾼 후 팁을 구하면 그것이 최대이다.

n = int(input())  # 손님의 수
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

tip = 0
for i in range(len(lst)):
    s = 0

    s = (lst[i] - ((i+1)-1))
    if s < 0:
        tip += 0
    else:
        tip += s

print(tip)
