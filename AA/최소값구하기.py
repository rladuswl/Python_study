arr = [5, 3, 7, 9, 2, 5, 2, 6]

arrMin = float('inf')  # 최소값을 나타내는 변수, inf는 파이썬에서 가장 큰 값
# arrMin = arr[0]  # 이렇게 초기화해도 됨

for i in range(len(arr)):
    if arrMin > arr[i]:
        arrMin = arr[i]

print(arrMin)