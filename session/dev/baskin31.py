import random

x= random.choice([1,2,3,4,5,6])
y = random.choice([1,2,3,4,5,6])

call = 0
count = 0
while call < 31:
  if x<y:
    print('사용자의 차례')
    user_call = int(input("숫자를 입력").split())
    
    for i in range(user_call):
      call +=1
      print("사용자: '{0}".format(call))

  elif(x==y):
    continue

  else:
    print('컴퓨터의 차례')
    com_call = ranom.randint(1,3)
    
    for i in range(com_call):
      call+=1
      print("컴퓨터: {0}".format(call))

  count +=1


  
if count % 2 == order:
    print("사용자의 승리!!")
else:
    print("컴퓨터의 승리!!")
    