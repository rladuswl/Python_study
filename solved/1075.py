n = input()
f = int(input())

nn = ''
for i in range(len(n)-2):
    nn = nn + n[i]

nn = nn + '00'
nn = int(nn)

while nn % f != 0:
    nn += 1

nn = str(nn)

for i in range(len(nn)-2, len(nn)):
    print(nn[i], end='')