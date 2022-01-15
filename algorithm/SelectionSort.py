# 선택 정렬
# 가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘
# 선택 정렬의 시간 복잡도는 O(N^2)

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(0, 10, 1):
    min = 9999
    for j in range(i, 10, 1):
        if min > array[j]:
            min = array[j]
            index = j
    temp = array[i]
    array[i] = array[index]
    array[index] = temp

for i in range(0, 10, 1):
    print(array[i], end=" ")
