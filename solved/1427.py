# 백준 1427 소트인사이드
import sys

n = sys.stdin.readline().rstrip()

print(''.join(sorted(n, reverse=True)))