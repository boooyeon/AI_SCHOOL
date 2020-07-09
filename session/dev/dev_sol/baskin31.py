# 베스킨라빈스 31 인공지능화하기!

# 30을 사용자가 무조건 부를수있게 하는 것

# 2, 6, 10, 14, 18, 22, 26, 30 하나만 사용자가 부르기 시작해도 이어서 그 다음을 부를 수 있기에 무조건 승리

# https://blog.naver.com/jong1003min/220348353765

# 위 숫자들은 +2 혹은 -2를 한 뒤에 4로 나누면 무조건 나머지가 0인 숫자들

from random import randrange

picked_list = []
whos_first = randrange(0, 2)


def computer_pick():
    computer_pick = randrange(1, 4)
    if (picked_list):
        if (picked_list[-1] + computer_pick >= 31):
            picked_list.append(31)
        else:
            picked_list.append(picked_list[-1] + computer_pick)
    else:
        picked_list.append(computer_pick)
    print('컴퓨터가 마지막에 부른 수 : %d' % (picked_list[-1]))


def player_pick():
    if (picked_list):
        number = 0
        player_pick = randrange(1, 4)
        if (((picked_list[-1] + 1) + 2) % 4 == 0):
            number = picked_list[-1] + 1
        elif (((picked_list[-1] + 2) + 2) % 4 == 0):
            number = picked_list[-1] + 2
        elif (((picked_list[-1] + 3) + 2) % 4 == 0):
            number = picked_list[-1] + 3
        else:
            number = picked_list[-1] + player_pick
        picked_list.append(number)
    else:
        player_pick = 2
        picked_list.append(player_pick)
    print('플레이어가 마지막에 부른 수 : %d' % (picked_list[-1]))


while(True):
    if (whos_first == 0):
        player_pick()
        computer_pick()
        if (picked_list[-1] == 31):
            print("플레이어 승리!")
            break
    elif (whos_first == 1):
        computer_pick()
        if (picked_list[-1] == 31):
            print("플레이어 승리!")
            break
        player_pick()