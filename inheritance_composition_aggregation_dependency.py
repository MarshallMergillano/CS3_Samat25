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

# Composition
