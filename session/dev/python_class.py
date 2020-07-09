class Game:
  def __init__(self,name,hp,mp):
    self.name = name
    self.hp = hp
    self.mp = mp
  
  def attack(self):
    self.hp -= 50
  
  def defense(self):
    self.hp += 100
  
  def skill(self,p1):
    self.mp -= 100
    p1.hp -= 100

player1 = Game("김보연", 100, 100)
player2 = Game("김신영", 200, 200)
player3 = Game("김주연", 300, 300)

player1.attack()
print(player1.hp)
player2.skill(player1)
print(player1.hp)
print(player2.mp)
