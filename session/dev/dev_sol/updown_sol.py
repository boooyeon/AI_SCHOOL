# 컴퓨터가 임의의 수(C)를 정했다.

# 플레이어(컴퓨터)가 임의의 수(P)를 정했다.

# 컴퓨터가 플레이어의 수보다 자신의 수가 높은지 낮은지를 출력한다.

# C>P 컴퓨터는 업이라고 할거고 100까지니까 100~P 사이를 2로 나눠서 그 중간에 있는 값을 다음에 대입한다.

# C<P 컴퓨터는 다운이라고 할거고 0까지니까 0~P 사이를 2로 나눠서 그 중간에 있는 값을 다음에 대입한다.

# 남아있는 수 중에 중간을 찾아간다.

from random import randrange

#컴퓨터가 임의의 수를 뽑는다.
picked_number = randrange(1, 101)

#우리는 컴퓨터가 뽑을 수 있는 수가 1~100까지라는 걸 알기때문에
#뽑을 수 있는 수에 해당하는 리스트를 만듭니다.
list_100 = []
for i in range(1, 101):
    list_100.append(i)

#업, 다운일 경우에 플레이어가 선택한 가장 마지막값
#[가장 업, 가장 다운]

for i in range(0, 100):
    if (i == 0):
        user_input = randrange(1, 101)
    else:
        user_input = x
    print(user_input)
    if (user_input == picked_number):
        print("맞췄네요!")
        break
    elif (user_input > picked_number):
        print("다운")
        user_index = list_100.index(user_input)
        del list_100[user_index:]
        x = list_100[int(len(list_100)/2)]
    else:
        print("업")
        user_index = list_100.index(user_input)
        del list_100[:user_index]
        x = list_100[int(len(list_100)/2)]

print('실제값:', picked_number)
 