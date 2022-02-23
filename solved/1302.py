# 백준 1302 베스트셀러

import sys

n = int(sys.stdin.readline())

book_dict = {}
for _ in range(n):
    book = sys.stdin.readline().rstrip()

    if book in book_dict.keys():
        book_dict[book] += 1
    else:
        book_dict[book] = 1

m = max(book_dict.values())

m_list = []
for k, v in book_dict.items():
    if v == m:
        m_list.append([k, v])

m_list.sort(key= lambda x : x[0])

print(m_list[0][0])