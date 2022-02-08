# 다이나믹 프로그래밍
# 효율적인 화폐 구성
# 못풀음
'''내 풀이
n, m = map(int, input().split())

k = list(int(input()) for _ in range(n))

# 최소 화폐 개수
d = [0]
for i in range(1, m+1):
    # 화폐가치 m은 최대가 10,000 이므로 만약 1원 화폐를 가졌을 때 필요한 최소 화폐 개수는 10,000개
    # 따라서 10,001개로 설정해서 여기서부터는 어떤 m보다도 큰 화폐 가치가 나옴 = 무한
    # -> 특정 금액을 만들 수 있는 화폐 구성이 존재하지 않음
    d.append(10001)

for x in k:
    for i in range(x, len(d)):
        # 조건문 넣어줘야함..
        d[i] = min(d[i-x]+1, d[i])

# 계산된 결과 출력
if d[m] == 10001:  # m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
'''

'''유튜브 풀이'''
n, m = map(int, input().split())

# n개의 화폐 단위 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001] * (m+1)
d[0] = 0

# 다이나믹 프로그래밍 진행 (보텀업)
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)

# 계산된 결과 출력
if d[m] == 10001:  # m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
