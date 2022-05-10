def LinearHashInsert(hash_table, x):
    global Lcnt
    hv = x % len(hash_table)

    if (hash_table[hv] == -1):
        hash_table[hv] = x
    else:
        for j in range(len(hash_table)):
            t = (hv + j) % len(hash_table)

            if (hash_table[t] == -1):
                hash_table[t] = x
                break
            Lcnt += 1


def LinearHashSearch(hash_table, x):
    global c
    hv = x % len(hash_table)

    if (hash_table[hv] == x):
        c+=1
        return hv
    else:
        for j in range(len(hash_table)):
            c += 1
            t = (hv + j) % len(hash_table)

            if (hash_table[t] == x):
                return t
        else:
            return -1

def quadraticHashInsert(hash_table, x):
    global Qcnt
    hv = x % len(hash_table)

    if (hash_table[hv] == -1):
        hash_table[hv] = x
    else:
        for j in range(len(hash_table)):
            t = (hv + j*j) % len(hash_table)

            if (hash_table[t] == -1):
                hash_table[t] = x
                break
            Qcnt += 1


def quadraticHashSearch(hash_table, x):
    global c
    hv = x % len(hash_table)

    if (hash_table[hv] == x):
        c+=1
        return hv
    else:
        for j in range(len(hash_table)):
            c += 1
            t = (hv + j*j) % len(hash_table)

            if (hash_table[t] == x):
                return t
        else:
            return -1

import random

arr = random.sample(range(1, 150), 20)
print(arr)
LinearArray = arr  # 선형 조사에서 사용할, 원소가 20개인 난수 배열
QuadraticArray = arr  # 이차원 조사에서 사용할, 원소가 20개인 난수 배열

L = 31  # 저장소 개수
Linear_hash_table = [-1] * L  # 저장소를 모두 -1 로 초기화 시키기
Quadratic_hash_table = [-1] * L

# 선형 조사 방법으로 insert 하기
Lcnt = 0  # 충돌횟수
for x in LinearArray:  # 배열 값을 하나씩 insert 시키기
    LinearHashInsert(Linear_hash_table, x)

print('insert 완료한 해싱 테이블 :', end=' ')
for m in Linear_hash_table:  # insert 완료한 해싱 테이블 출력
    print(m, end=' ')
print()
print('충돌 횟수 :', Lcnt)

print('--------------')

# 선형 조사 방법으로 검색하기
for x in LinearArray:
    c = 0  # 조사 횟수
    result = LinearHashSearch(Linear_hash_table, x)
    if result == -1:
        print('검색 실패')
    else:
        print(x, '의 검색 자리 :', result)
        print(x, '의 검색 횟수 :', c)
        print('----')


print('-------------------이차원 조사------------------------')
# 이차원 조사 방법으로 insert 하기
Qcnt = 0  # 충돌횟수
for x in QuadraticArray:  # 배열 값을 하나씩 insert 시키기
    quadraticHashInsert(Quadratic_hash_table, x)

print('insert 완료한 해싱 테이블 :', end=' ')
for m in Quadratic_hash_table:  # insert 완료한 해싱 테이블 출력
    print(m, end=' ')
print()
print('충돌 횟수 :', Qcnt)

print('--------------')

# 이차원 조사 방법으로 검색하기
for x in QuadraticArray:
    c = 0  # 조사 횟수
    result = quadraticHashSearch(Quadratic_hash_table, x)
    if result == -1:
        print('검색 실패')
    else:
        print(x, '의 검색 자리 :', result)
        print(x, '의 검색 횟수 :', c)
        print('----')