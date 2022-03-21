''' 3주차 과제
# selection sort
# 가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘
# 선택 정렬의 시간 복잡도는 O(N^2)
def selectionSort(A, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]  # swap 하기

# bubble sort
# 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내기
# 버블 정렬의 시간 복잡도는 O(N^2)
def bubbleSort(A):
    for i in range(len(A)):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]



# insertion sort
# 각 숫자를 적절한 위치에 삽입하기
# 삽입 정렬의 시간 복잡도는 O(N^2)
def insertionSort(A):
    for e in range(1, len(A)):
        i = e
        while i > 0 and A[i - 1] > A[i]:
            A[i - 1], A[i] = A[i], A[i - 1]
            i -= 1

# merge sort
# 일단 반으로 나누고 나중에 합쳐서 정렬하기
# 병합 정렬의 시간 복잡도는 O(N * logN)
def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2

        L = A[:mid]  # 인덱스 : 0~(mid-1)
        R = A[mid:]  # 인덱스 : min~(len(A)+1)

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

import random
import time

# 1~200의 배열A 만들기
A = list()
for _ in range(200):
    A.append(random.randint(1, 200))

print('정렬 전 배열A:', A)

start = time.time()  # 시작 시간 측정
mergeSort(A)  # mergeSort 함수 호출
end = time.time()  # 끝난 시간 측정

print('정렬 후 배열A:', A)
print('걸린 시간:', end-start, 'sec')
print('103번째 원소:', A[100-1])

'''

# merge sort
# 일단 반으로 나누고 나중에 합쳐서 정렬하기
# 병합 정렬의 시간 복잡도는 O(N * logN)
def mergeSort(B):
    if len(B) > 1:
        mid = len(B) // 2

        L = B[:mid]  # 인덱스 : 0~(mid-1)
        R = B[mid:]  # 인덱스 : min~(len(A)+1)

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                B[k] = L[i]
                i += 1
            else:
                B[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            B[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            B[k] = R[j]
            j += 1
            k += 1

import time

# 1~200의 배열B 만들기 (이미 정렬이 된 오름차순 배열)
B = list()
for i in range(1, 200+1):
    B.append(i)

print('정렬 전 배열B:', B)

start = time.time()  # 시작 시간 측정
mergeSort(B)  # mergeSort 함수 호출
end = time.time()  # 끝난 시간 측정

print('정렬 후 배열B:', B)
print('걸린 시간:', end-start, 'sec')


# selection sort
# 가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘
# 선택 정렬의 시간 복잡도는 O(N^2)
def selectionSort(B):
    for i in range(len(B)-1):
        for j in range(i+1, len(B)):
            if B[i] > B[j]:
                B[i], B[j] = B[j], B[i]  # swap 하기


# bubble sort
# 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내기
# 버블 정렬의 시간 복잡도는 O(N^2)
def bubbleSort(B):
    for i in range(len(B)):
        for j in range(0, len(A)-1-i):
            if B[j] > B[j + 1]:
                B[j + 1], B[j] = B[j], B[j + 1]



# insertion sort
# 각 숫자를 적절한 위치에 삽입하기
# 삽입 정렬의 시간 복잡도는 O(N^2)
def insertionSort(B):
    for e in range(1, len(B)):
        i = e
        while i > 0 and A[i - 1] > B[i]:
            B[i - 1], B[i] = B[i], B[i - 1]
            i -= 1



# merge sort
# 일단 반으로 나누고 나중에 합쳐서 정렬하기
# 병합 정렬의 시간 복잡도는 O(N * logN)
def mergeSort(B):
    if len(B) > 1:
        mid = len(B) // 2

        L = B[:mid]  # 인덱스 : 0~(mid-1)
        R = B[mid:]  # 인덱스 : min~(len(A)+1)

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                B[k] = L[i]
                i += 1
            else:
                B[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            B[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            B[k] = R[j]
            j += 1
            k += 1