color1 = input()
color2 = input()
color3 = input()

clist = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
value = [x for x in range(len(clist))]
mul = [10**x for x in range(0, len(clist))]
sa = ''
result = 0
for i in range(len(clist)):
    if color1 == clist[i]:
        sa = sa + str(value[i])
        for j in range(len(clist)):
            if color2 == clist[j]:
                sa = sa + str(value[j])
            for k in range(len(clist)):
                if color3 == clist[k]:
                    result = int(sa) * mul[k]

print(result)