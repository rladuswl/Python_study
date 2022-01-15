# 버블 정렬
# 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내기
# 버블 정렬의 시간 복잡도는 O(N^2)

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(0, 10, 1):
    for j in range(0, 9-i, 1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

for i in range(0, 10, 1):
    print(array[i], end=" ")

'''
import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 5) # 1<= x < 10의 난수 5개 리스트로 생성
print(a) # 정렬 전 리스트
print('')
for i in range(1, len(a)): # 리스트의 크기만큼 반복
    for j in range(0, len(a)-1): # 각 회전당 정렬이 끝나지 않은 친구들을 위해 반복
        if a[j] > a[j+1]: # 현재 인덱스의 값이 다음 인덱스의 값보다 크면 실행
           a[j+1], a[j] = a[j], a[j+1] # swap해서 위치 바꾸기
print('')
print(a) # 정렬 후 리스트

#출력
[4, 9, 2, 5, 7]


[2, 4, 5, 7, 9]
'''