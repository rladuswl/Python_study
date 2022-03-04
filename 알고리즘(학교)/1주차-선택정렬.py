## 1주차 3번 문제
# 선택 정렬
# 가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘
# 선택 정렬의 시간 복잡도는 O(N^2)

# ------------------
'''
import time
import datetime
import timeit
import random

n = 10
for i in range(n):
        A = random.sample(range(1, n+1), n)  # Random number generator 사용

# 선택 정렬 수행

start = timeit.default_timer()  # 시작 시간 저장

print('선택 정렬 전 : ', A)
for i in range(len(A)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(A)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if A[i] > A[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            A[i] , A[j]  = A[j], A[i] # swap 해주기
print('선택 정렬 후 : ', A)

end = timeit.default_timer()  # 끝나는 시간 저장

print('실행시간 : ', end-start)  # end시간 - start시간 = 실행 시간
'''
# ------------------
'''
import time
import datetime
import timeit
import random

n = 100
for i in range(n):
        A = random.sample(range(1, n+1), n)  # Random number generator 사용

# 선택 정렬 수행

start = timeit.default_timer()  # 시작 시간 저장

print('선택 정렬 전 : ', A)
for i in range(len(A)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(A)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if A[i] > A[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            A[i] , A[j]  = A[j], A[i] # swap 해주기
print('선택 정렬 후 : ', A)

end = timeit.default_timer()  # 끝나는 시간 저장

print('실행시간 : ', end-start)  # end시간 - start시간 = 실행 시간
'''
# ------------------
'''
import time
import datetime
import timeit
import random

n = 1000
for i in range(n):
        A = random.sample(range(1, n+1), n)  # Random number generator 사용

# 선택 정렬 수행

start = timeit.default_timer()  # 시작 시간 저장

print('선택 정렬 전 : ', A)
for i in range(len(A)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(A)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if A[i] > A[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            A[i] , A[j]  = A[j], A[i] # swap 해주기
print('선택 정렬 후 : ', A)

end = timeit.default_timer()  # 끝나는 시간 저장

print('실행시간 : ', end-start)  # end시간 - start시간 = 실행 시간

'''

# ------------------
'''
import time
import datetime
import timeit
import random

n = 10000
for i in range(n):
        A = random.sample(range(1, n+1), n)  # Random number generator 사용

# 선택 정렬 수행

start = timeit.default_timer()  # 시작 시간 저장

print('선택 정렬 전 : ', A)
for i in range(len(A)-1): # 리스트의 크기-1만큼 반복
    for j in range(i+1, len(A)): # 해당 인덱스+1부터, 리스트 크기만큼 반복
        if A[i] > A[j]: # 인덱스의 값이 비교 인덱스보다 더 크다면
            A[i] , A[j]  = A[j], A[i] # swap 해주기
print('선택 정렬 후 : ', A)

end = timeit.default_timer()  # 끝나는 시간 저장

print('실행시간 : ', end-start)  # end시간 - start시간 = 실행 시간
'''