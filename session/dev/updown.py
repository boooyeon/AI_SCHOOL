import random

x= int(random.random()*100)+1

y = int(random.random()*100)+1
print(x,y)
pibot=y
for i in range(50):
  if(x==y):
    print("정답")
    break
  elif(x>y):
    print("up")
    z=100-y
    y= y+int(random.random()*z)+1
  elif(x<y):
    print("down")
    z=100-y
    y= y-int(random.random()*z)+1
    