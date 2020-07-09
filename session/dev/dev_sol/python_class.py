class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
    def attack(self, target):
        target.hp = target.hp - 10
        if (target.hp < 0):
            print("%s을 죽였습니다!" % target.name)
        else:
            print("%s의 HP가 %d이 되었습니다" % (target.name, target.hp))
    def skill(self, target):
        target.hp = target.hp - 100
        if (target.hp <= 0):
            print("%s을 죽였습니다!" % target.name)
        else:
            print("%s의 HP가 %d이 되었습니다" % (target.name, target.hp))   
    def defend(self, target):
        target.hp = target.hp + 50

Player1 = Player('First', 100, 100)
Player2 = Player('Second', 100, 100)
Player3 = Player('Third', 100, 100)

Player1.skill(Player2)
Player3.attack(Player1)