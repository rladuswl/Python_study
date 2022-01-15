# 퀵 정렬
# 특정한 값을 기준으로 큰 숫자와 작은 숫자 나누기
# 퀵 정렬의 시간 복잡도는 O(N * logN)
# 기준 값(피벗)보다 큰 숫자를 왼쪽부터 찾고, 작은 숫자를 오른쪽부터 찾기

number = 10
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

def quickSort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 그대로 두기
        return

    key = start  # 키는 첫 번째 원소
    i = start + 1
    j = end

    while i <= j: # 엇갈릴 때까지 반복
        while i <= end and array[i] <= array[key]:  # 키 값보다 큰 값을 만날 때까지
            i+=1
        while j > start and array[j] >= array[key]:  # 키 값보다 작은 값을 만날 때까지
            j-=1

        if i > j:  # 현재 엇갈린 상태이면 키 값과 교체
            temp = array[j]
            array[j] = array[key]
            array[key] = temp
        else:  # 엇갈리지 않았다면 i와 j를 교체
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    quickSort(array, start, j - 1)
    quickSort(array, j + 1, end)


quickSort(array, 0, number - 1)

print(array)


'''
import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 5) # 1<= x < 10의 난수 5개 리스트로 생성
print(a) # 정렬 전 리스트
print('')
def quickSort(a, start, end):# 재귀함수용 함수 선언(리스트, 시작인덱스, 종료인덱스)
    # print(a)
    if start < end: # 시작 인덱스 보다 끝 인덱스가 클 경우
        left = start # left 변수에 시작 인덱스 할당
        pivot = a[end] #  //pivot 값은 a리스트에 마지막 원소 값
        for i in range(start, end): # 시작인덱스부터 끝 원소까지 반복
            if a[i] < pivot: # 리스트 인덱스 값이 pivot 값보다 작을 경우라면
                a[i], a[left] = a[left], a[i] #  해당 인덱스와 left인덱스  swap
                left += 1 # 인덱스 하나 증가 시켜주기(자리를 옮겨가며 비교해야 하기 때문에)
        a[left] , a[end] = a[end], a[left] # left인덱스와 끝 인덱스 swap
        print(left)
        quickSort(a, start, left-1) # 재귀 호출 (리스트, 시작 인덱스, left-1)
        quickSort(a, left+1, end) # 재귀 호출 (리스트, left+1, 종료인덱스)
quickSort(a, 0, len(a)-1)
print('')
print(a) # 정렬 후 리스트

#출력
[8, 1, 7, 2, 5]


[1, 2, 5, 7, 8]
'''