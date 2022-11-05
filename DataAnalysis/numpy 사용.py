import numpy as np


def main():
    Score = np.random.randint(100, size=(10, 4))  # 국어, 영어, 수학, 과학
    print('Score')
    print(Score)
    print()
    mathScore(Score)
    sumScore(Score)
    oddStudent(Score)
    maxScore(Score)
    engScore(Score)


def mathScore(Score):  # 문제 1 : 모든 학생의 수학 점수만을 출력
    print('문제 1')
    print(Score[:, 2])
    print()


def sumScore(Score):  # 문제 2 : 각 학생의 과목의 총합 점수
    print('문제 2')
    print(Score.sum(axis=1))
    print()


def oddStudent(Score):  # 문제 3 : 불린 인덱스를 이용하여 홀수 번째 학생의 점수를 과학, 수학, 국어, 영어의 순으로 출력(5x4)
    boolean_index = [False, True, False, True, False, True, False, True, False, True]
    odd = Score[boolean_index]
    # print(odd)
    change_index = odd[:, [3, 2, 0, 1]]
    # print(change_index)
    print('문제 3')
    print(change_index)
    print()


def maxScore(Score):  # 문제 4 : 각 과목에서의 최대 점수
    print('문제 4')
    print(np.max(Score, axis=0))
    print()


def engScore(Score):  # 문제 5 : 영어 과목이 90점 미만인 학생들의 점수 (boolean사용)
    under_ninety = Score[:, 1] < 90
    # print(under_ninety) - boolean 값
    print('문제 5')
    print(Score[under_ninety])
    print()


main()