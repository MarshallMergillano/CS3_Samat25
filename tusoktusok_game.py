Class Tusoktusok:
  name = ""
  sauce = None
def __init__(self,name):
  self.name = name
def dip(self,sauce):
  self.sauce = sauce
def eat(self):
  print("I ate",self.name,"with",self.sauce.name,"and it tastes",self.sauce.taste)

Class Sauce:
  name = ""
  taste = ""
def __init__(self,name,taste):
  self.name =name
  self.taste = taste

fishball = Tusoktusok("fishball")
vinegar = Sauce("vinegar","sour")
fishball.dip(vinegar)
fishball.eat()
