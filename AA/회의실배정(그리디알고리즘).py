import sys
#sys.stdin = open("input.txt", "rt")

# 못 풀음
# 그리디 : 각 단계에서 가장 좋은 것 판별하기
# 정렬과 동반되어 사용

## 회의실 배정(그리디)
# 회의를 최대한 많이 하기 위해서는 끝나는 시간으로 정렬해야 한다.
'''모범답안'''
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))  # 튜플 형태로 리스트에 넣기
meeting.sort(key = lambda x : (x[1], x[0]))  # 람다 함수 - 첫 순위는 x[1], 다음 순위는 x[0]
et = 0  # end time
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)
