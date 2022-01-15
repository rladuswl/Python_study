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