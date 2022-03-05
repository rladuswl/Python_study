## 키워드
''' 풀음
def main():
    t = int(input())
    ing = []
    for _ in range(t):
        ing.append(input())

    for i in range(len(ing)):
        cnt = 0
        for j in range(len(key)):
            if key[j][0:len(ing[i])] == ing[i]:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    n = int(input())  # 키워드 개수
    key = []
    for _ in range(n):
        key.append(input())
    main()
'''

## 산사태 셋
''' 못품 ㅠ
def avalanche(s, key_memory):
    for k, v in key_memory[s]:
    key_memory[s+1].append({})
    for i in range(len(lev[s])):
        if lev[s][i] in lev[s+1]:
            lev_size[s+1] -= key_memory[s]

        lev[s+1].append(lev[s])
        lev_size[s+1] += lev_size[s]
        lev_size[s] -= lev_size[s]

    if lev_size[s+1] > origin_lev_size[s+1]:
        avalanche(s+1, key_memory)


def insert(k, s):
    global lev_size
    key_memory[k] = s
    if k in key_memory.keys():
        lev_size[0] -= key_memory[k]
    key_memory[k] = s
    lev_size[0] += s
    lev[0].append(k)

    if lev_size > origin_lev_size:
        return '1'
    else:
        return '0'



def find(k):
    for i in range(len(lev)):
        for j in range(len(lev[i])):
            if lev[i][j] == k:
                return i+1, lev_size[i]
            else:
                return 'none'


if __name__ == "__main__":
    n, q = map(int, input().split())
    origin_lev_size = list(map(int, input().split()))
    lev = []
    for i in range(n):
        lev.append([])

    key_memory = {}
    lev_size = [0]*(n-1)
    for _ in range(q):
        a = list(input().split())
        if len(a) == 3:
            a[1] = int(a[1])
            a[2] = int(a[2])
            if insert(int(a[1]), int(a[2])) == '1':
                avalanche(0, key_memory)

        elif len(a) == 2:
            a[1] = int(a[1])
            print(find(a[1]))
'''

# 식단 짜기
'''풀음
def main(L, s, sum):
    global cnt
    if L == 3:
        if 2000 <= sum <= 2500:
            cnt += 1
    else:
        for i in range(s, len(lst)):
            main(L+1, i+1, sum+lst[i])


if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    main(0, 0, 0)
    print(cnt)
'''