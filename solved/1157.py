# 문자열
# 단어 공부
# 1157번

'''백준 채점 결과가 틀렸다고 나오는 이유 모름 ㅠㅠ 맞는데..
s = input()
s_upper = s.upper()
s_dict = {}
for i in range(len(s_upper)):
    if s_upper[i] not in s_dict.keys():
        s_dict[s_upper[i]] = 1
    else:
        s_dict[s_upper[i]] += 1

max = 0
for key, value in s_dict.items():
    if value > max:
        max = value
        k = key
    elif value == max:
        print("?")
        break
else:
    print(k)
'''

s = input().upper() # [M, I, S, S, I, S, S, I , P ,I]
s_set_list = list(set(s)) # [M, I, S, P]
s_list = []
for i in s_set_list:
    s_list.append(s.count(i)) # [1, 4, 4, 1]

if s_list.count(max(s_list)) > 1:
    print("?")
else:
    print(s_set_list[s_list.index(max(s_list))])