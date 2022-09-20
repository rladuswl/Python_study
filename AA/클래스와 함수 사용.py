import sys
#sys.stdin = open("input.txt", "rt")
#input = sys.stdin.readline

import random

def main():
    r1 = Rectangle(True, 3, 3, 3)
    print('1번 문제 : 부피', r1.getVolume())

    calculateGrade()
    listAverage()

class Rectangle:  # 문제 1
    def __init__(self, isCube, length, height, weight):
        self.__isCube = isCube
        self.__length = length
        self.__height = height
        self.__weight = weight

    def setIsCube(self, isCube):
        self.__isCube = isCube

    def setLength(self, length):
        self.__length = length

    def setHeight(self, height):
        self.__height = height

    def setWeight(self, weight):
        self.__weight = weight

    def getVolume(self):
        if self.__isCube == True:
            return self.__length * self.__length * self.__length
        else:
            return self.__length * self.__height * self.__weight

def calculateGrade():  # 문제 2
    # A, B, C, D, E (65, 66, 67, 68, 69)
    student = []
    answer = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    result = []

    for i in range(8):
        rd = [chr(random.randint(65, 69)) for r in range(10)]
        student.append(rd)

    for x in range(8):
        cnt = 0
        for y in range(10):
            if student[x][y] == answer[y]:
                cnt += 1
        result.append(cnt)

    print('2번 문제 :')
    for a in range(8):
        print(a, '번 학생의 정답 문항의 개수는', result[a], '입니다.')

def listAverage():  # 문제 3
    avg = []

    lst1 = []
    for x in range(10):
        lst1.append(int(random.random() * 10))

    lst2 = []
    for x in range(10):
        lst2.append(int(random.random() * 10))

    for i in range(10):
        result = lambda x, y : (x+y)/2
        avg.append(result(lst1[i], lst2[i]))

    print('3번 문제 : 평균', avg)

main()
