import sys
input = sys.stdin.readline

str = input().rstrip()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in alpha:
    str = str.replace(x, '.')

print(len(str))