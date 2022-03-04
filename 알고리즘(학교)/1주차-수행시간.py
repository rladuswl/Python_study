## 1주차 1번 문제

## n에 관계없이 상수 시간 소요
'''
import time
from datetime import timedelta

start = time.time()  # 시작 시간 저장

# 작업 코드
k = 1000000000000//2

end = time.time()  # 끝나는 시간 저장

print('실행시간 : ', timedelta(seconds=end-start))  # end시간 - start시간 = 실행 시간
print('실행시간 : ', end-start)

# -> 측정 결과 : n이 10, 100, ..., 100000000 까지 커져도 상수시간이 소요된다.
'''

## n에 비례하는 시간 소요
'''
import time
from datetime import timedelta

start = time.process_time()  # 시작 시간 저장

# 작업 코드
sum = 0
for i in range(1000000):
    sum += i

end = time.process_time()  # 끝나는 시간 저장

print('실행시간 : ', timedelta(seconds=end-start))  # end시간 - start시간 = 실행 시간
print('실행시간 : ', end-start)
'''

## n제곱에 비례하는 시간 소요
'''
from timeit import default_timer as timer
from datetime import timedelta

start = timer()  # 시작 시간 저장

# 작업 코드
sum = 0
for i in range(1000):
    for j in range(1000):
        sum += (i*j)

end = timer()  # 끝나는 시간 저장

print('실행시간 : ', timedelta(seconds=end-start))  # end시간 - start시간 = 실행 시간
print('실행시간 : ', end-start)
'''


## n세제곱에 비례하는 시간 소요

from timeit import default_timer as timer
from datetime import timedelta

start = timer()  # 시작 시간 저장

# 작업 코드
sum = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            sum += (i*j*k)

end = timer()  # 끝나는 시간 저장

print('실행시간 : ', timedelta(seconds=end-start))  # end시간 - start시간 = 실행 시간
print('실행시간 : ', end-start)