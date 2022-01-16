import sys
# sys.stdin = open("input.txt", "rt")

## K번째 약수
N, K = map(int, input().split())

n = 0  # 약수의 개수

for i in range(1, N+1):
    if N%i == 0:  # N의 약수라면
        n+=1
    if n>=K:
        print(i)
        break
else:  # for문 안에서 break를 당하지 않고 나오면(for문 끝까지 돌고 나오면) for-else 실행
    print(-1)

'''해답
if n<K:
    print(-1)
'''