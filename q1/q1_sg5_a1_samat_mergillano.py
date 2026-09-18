class Hero:
  def __init__(self,name,hp):
    self.name = name
    self.hp = hp
  def take_damage(self,amount):
    self.hp -= amount
    print(self.name,"has",self.hp,"hp left")

arthur = Hero("Arthur",100)
morgana = Hero("Morgana",100)
arthur.take_damage(10)
morgana.take_damage(0)
