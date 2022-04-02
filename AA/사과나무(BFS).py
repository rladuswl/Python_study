import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

