# n이 0, 1, 2 일 때까지의 0과 1의 호출 횟수를 미리 저장
zero = [1, 0, 1]
one = [0, 1, 1]

def f(n):
    # 배열을 만들어서 값을 저장하므로 이미 구한 숫자를 또 구할 일이 없다
    # zero와 one 배열은 전역 변수이기 때문에 길이가 계속 바뀐다
    # 따라서 배열 길이로부터 n의 기준이 계속 바뀌어야 한다.
    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n], one[n])

t = int(input())
for _ in range(t):
    n = int(input())
    f(n)