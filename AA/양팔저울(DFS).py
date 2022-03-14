import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 양팔저울 (DFS)
# 어렵다!!!!

def DFS(L, s):
    if L == k:
        if s > 0:  # 0<s<=k_sum
            s_set.add(s)
    else:
        #for i in range(L, len(k_list)):
            DFS(L+1, s+k_list[L])  # 저울의 왼쪽(+)
            DFS(L+1, s-k_list[L])  # 저울의 오른쪽(-)
            DFS(L+1, s)  # 추 사용 X

if __name__ == '__main__':
    k = int(input())
    k_list = list(map(int, input().split()))
    k_sum = sum(k_list)  # 추의 무게의 총 합
    s_set = set()  # 측정될 수 있는 물의 무게
    DFS(0, 0)
    print(k_sum - len(s_set))