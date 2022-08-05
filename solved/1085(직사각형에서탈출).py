import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

lst = []

# x, w
if x>=w/2:
    lst.append(w-x)
else:
    lst.append(x)

# y, h
if y>=h/2:
    lst.append(h-y)
else:
    lst.append(y)

print(min(lst))