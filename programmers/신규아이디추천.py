# 1. 입력받은 문자열에서 대문자 찾아 소문자로 변경
# 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 를 제외한 모든 문자 제거
# 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
# 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
# 5. 빈 문자열이라면 'a' 대입
# 6. 길이가 16자 이상이면, 문자열의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
#    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
# 7. 길이가 2자 이하라면, 문자열의 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임

'''
def solution(new_id):

    # 1
    answer1 = ''
    for i in range(len(new_id)):
        if 65 <= ord(new_id[i]) <= 90:  # 만약 아스키코드로 변환했을 때 대문자 범위에 있다면
            answer1 += chr(ord(new_id[i]) + 32)
        else:
            answer1 += new_id[i]
    # print('1', answer1)

    # 2
    answer2 = ''
    for i in range(len(answer1)):
        if 97 <= ord(answer1[i]) <= 122:  # 소문자라면
            answer2 += answer1[i]
        elif answer1[i].isdecimal():  # 숫자라면
            answer2 += answer1[i]
        elif answer1[i] == '-' or answer1[i] == '_' or answer1[i] == '.':
            answer2 += answer1[i]
        else:
            continue
    # print('2', answer2)

    # 3
    answer3 = ''
    while '..' in answer2:
        answer2 = answer2.replace('..', '.')
    answer3 += answer2
    # print('3', answer3)


    # 4
    answer4 = ''
    if answer3[0] == '.' and answer3[-1] == '.':
        answer4 += answer3.strip('.')
    elif answer3[0] == '.':
        answer4 += answer3.lstrip('.')
    elif answer3[-1] == '.':
        answer4 += answer3.rstrip('.')
    else:
        answer4 = answer3
    # print('4', answer4)

    # 5
    answer5 = ''
    if len(answer4) == 0:
        answer5 += 'a'
    else:
        answer5 += answer4
    # print('5', answer5)

    # 6
    answer6 = ''
    if len(answer5) >= 16:
        answer6 += answer5[:15]
        if answer6[-1] == '.':
            answer6 = answer6.rstrip('.')
    else:
        answer6 += answer5
    # print('6', answer6)

    # 7
    answer7 = ''
    if len(answer6) <= 2:
        answer7 += answer6
        while True:
            if len(answer7) == 3:
                break
            answer7 += answer6[-1]
    else:
        answer7 += answer6
    # print('7', answer7)

    return answer7


new_id = input()
print(solution(new_id))
'''

def solution(new_id):
    answer = ''

    # 1. 입력받은 문자열에서 대문자 찾아 소문자로 변경
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 를 제외한 모든 문자 제거
    for x in new_id:
        if x.isalpha() or x.isdigit() or x in ['-', '_', '.']:
            answer += x

    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5. 빈 문자열이라면 'a' 대입
    if answer == '':
        answer = 'a'

    # 6. 길이가 16자 이상이면, 문자열의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(answer) > 15:
        answer = answer[:15]
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7. 길이가 2자 이하라면, 문자열의 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(answer) < 3:
        answer += answer[-1]

    return answer
