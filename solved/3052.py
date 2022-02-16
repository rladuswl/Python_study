# 백준 3052 나머지
# 수학, 사칙연산

lst = []
for _ in range(10):
    lst.append(int(input()))

for i in range(len(lst)):
    lst[i] = lst[i]%42

lst_set = set(lst)
print(len(lst_set))