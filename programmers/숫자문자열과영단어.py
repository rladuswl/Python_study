'''내 답안
def solution(s):
    d = [['0', 'zero'], ['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], ['5', 'five'], ['6', 'six'],
         ['7', 'seven'], ['8', 'eight'], ['9', 'nine']]
    s = list(s)
    answer = ''
    ss = []
    for i in range(len(s)):
        for j in range(len(d)):
            if s[i] == d[j][0]:
                for k in range(len(d[j][1])):
                    ss.append(d[j][1][k])
                break
        else:
            ss.append(s[i])

    a = ''
    for j in range(len(ss)):
        a = a + ss[j]
        for k in range(len(d)):
            if a == d[k][1]:
                answer = answer + d[k][0]
                a = ''

    return int(answer)
'''

'''모범답안1
d = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def solution(s):
    answer = s
    for key, value in d.items():
        answer = answer.replace(key, value)

    return int(answer)
'''

'''모범답안2
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = s
    for i in range(len(words)):
        answer = answer.replace(words[i], str(i))

    return int(answer)
'''