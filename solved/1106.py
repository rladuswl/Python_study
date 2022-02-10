# 1106 호텔
# 다이나믹 프로그래밍
# 참고 : https://castlerain.tistory.com/61
# 1e9 = 1*10^9 = 10억 = INF(무한)

INF = 1e9
c, n = map(int, input().split())
lst = []
for _ in range(n):
    # 비용, 고객 수
    lst.append(list(map(int, input().split())))

# 늘릴 수 있는 고객의 최대 수 1000 * 각 홍보 최대 비용 100
d = [INF] * (c+100)
d[0] = 0

# 비용이 작은 순서로 정리
lst_sort = sorted(lst, key = lambda x: x[0])

for a, b in lst_sort:  # a가 비용, b가 고객 수
    for i in range(b, c+100):
        d[i] = min(d[i-b]+a, d[i])
print(min(d[c:]))
