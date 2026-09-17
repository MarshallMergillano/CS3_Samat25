# INHERITANCE
class Vehicle:
  def __init(self,kindofvehicle):
    self.kindofvehicle = kindofvehicle
    print(self.kindofvehicle,"created")
  def move(self,distance):
    print(self.kindofvehicle,"moved",distance)

class Car(Vehicle):
  def __init__(self,kindofvehicle,brand,model):
    self.brand = brand; self.model = model
    super().__init__(kindofvehicle)
    print("I have a",self.brand,self.model)
  def move(self,distance):
    super().move(distance)
    print("KM")

class Boat(Vehicle):
  def __init__(self,kindofvehicle,model):
    self.model = model
    super().__init__(kindofvehicle)
    print("I have a",self.model)
  def move(distance):
    super().move(distance)
    print("Nm")

vios = Car("car","Toyota","Vios")
vios.move(67)
ferry = Boat("ferry","SS Thomas")
ferry.move(15)
yacht = Boat("yacht","Subid Yacht")
yacht.move(17)


# COMPOSITION
class Nucleus:
  def __init__(self):
    print("Nucleus is created")

class Mitochondria:
  def __init__(self):
    print("Mitochondria is created")

  def providePower(self):
    print("Mitochondria is powering the cell")

class Cell:
  def __init__(self):
    print("Cell is created")
    self.nucleus = Nucleus()
    self.mitochondria = Mitochondria()

def exist(self):
  print("Cell is existing")
  self.mitochondria.providePower()

def __del__(self):
  del self.nucleus
  del self.mitochondria
  print("Cell is gone")

cellAtWork = Cell()
cellAtWork.exist()
print(cellAtWork)
del cellAtWork
anotherCell = Cell()
print(anotherCell)



# AGGREGATION
class Sauce:
  def __init__(self,name,taste):
    self.name = name; self.taste = taste
    print(self.name,"is ready")
  def __del__(self):
    print(self.name,"is ubos na")

class Tusoktusok:
  def __init__(self,name,sauce):
    self.name = name
    self.sauce = sauce
    print(self.name,"is cooked and has",self.sauce.name)
  def eat(self):
    print("I am eating",self.name,"and it has",self.sauce.name)
  def __del__(self):
    print(self.name,"was thrown into the trash can")

hotsauce = Sauce("Hot sauce","spicy")
fishball = Tusoktusok("fishball", hotsauce)
del fishball
print(hotsauce.name)

    
# DEPENDENCY
class Sauce:
  def __init__(self,name,taste):
    self.name = name; self.taste = taste
    print(self.name,"is ready")
  def __del__(self):
    print(self.name,"is ubos na")

class Tusoktusok:
  def __init__(self,name,sauce = None):
    self.name = name
    self.sauce = sauce
    print(self.name,"is cooked")
    if self.sauce != None:
      print("It is dipped in",self.sauce)
  def eat(self):
    print("I am eating", self.name)
    if self.sauce != None:
    print("It tastes",self.sauce.taste)
  def dip(self,sauce):
    self.sauce = sauce
    print(self.name,"was dipped in",self.sauce)
  def __del__(self):
    print(self.name,"was thrown into the trash can")

hotsauce = Sauce("Hot sauce","spicy")
fishball = Tusoktusok("fishball", hotsauce)
fishball.eat()
kikiam = Tusoktusok("kikiam")
kikiam.eat() ;kikiam.dip(hotsauce); kikiam eat()
