# 백준 1343 폴리오미노

# 1. board판 str로 입력 받기
# 2. replace 함수로 XXXX를 AAAA 로 치환
# 3. replace 함수로 XX를 BB 로 치환
# 4. board에 x 가 남아있다면 -1, 아니면 board 출력

import sys
input = sys.stdin.readline

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

board_list = list(board)
if 'X' in board_list:
    print(-1)
else:
    print(board)