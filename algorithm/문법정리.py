# for-else 문
'''
for i in range(1, 11):
    print(i)
    if i==5:  # 정상 종료가 아님 (break 됨) -> else문 실행 X
        break
else:
    print(11)
'''

for i in range(1, 11):
    print(i)
    if i>15:  # 정상 종료임
        break
else:
    print(11)