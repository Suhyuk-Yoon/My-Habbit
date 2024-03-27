# 자료는 정수로 취급
# 입력값이 1에서 6 사이가 아니면 오류 처리
# 컴퓨터가 던진 주사위를 사람이 맞히기

from random import *
score = 0

while True:
    dice = randint(1, 6)

    h = int(input("얼마일까?"))

    if h < 1 or h > 6:
        print("오류")
    print("주사위는 ", dice, "입니다.")
    if h == dice:
        print("맞았습니다.")
        score = score+10
        print("점수는 ", score, "점 입니다.")
    else:
        print("틀렸습니다.")
        print("점수는 ", score, "점 입니다.")
        print("끝!")
        input()
        exit()


input()