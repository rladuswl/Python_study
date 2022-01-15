# 삽입 정렬
# 각 숫자를 적절한 위치에 삽입하기
# 삽입 정렬의 시간 복잡도는 O(N^2)
# 삽입 정렬은 '필요할 때에 한해서만' 삽입을 진행
# 데이터가 이미 거의 정렬된 상태에 한해서는 어떤 알고리즘보다도 빠른 특징

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(0, 9, 1):
    j = i
    while (j >= 0) and (array[j] > array[j + 1]):
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        j-=1

for i in range(0, 10, 1):
    print(array[i], end=" ")

'''
import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 5) # 1<= x < 11의 난수 5개 리스트로 생성
print(a)# 정렬 전 리스트
print('')
for i in range(1, len(a)): # 리스트의 크기만큼 반복
    for j in range(i, 0, -1): # j 인덱스의 값이 줄어드면서 삽입할 위치를 찾을 때까지 반복
        if a[j] < a[j-1]: # 현재 인덱스가 앞의 원소보다 작다면
            a[j], a[j-1] = a[j-1], a[j] # swap해서 값 뒤로 밀어내기
        else : break # 불필요한 반복을 피하기 위해 break
print('')
print(a) # 정렬 후 리스트 출력

#출력
[8, 9, 3, 1, 6]


[1, 3, 6, 8, 9]
'''