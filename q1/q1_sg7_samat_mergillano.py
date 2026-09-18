class Glassware:
  def __init__(self,kindofglassware = "Beaker"):
    self.kindofglassware = kindofglassware

class Beaker(Glassware):
  def __init__(self,kindofglassware = "Beaker"):
    super().__init__(kindofglassware)
    
class Tray:
  def __init__(self):
    self.tray = [Beaker() for i in range(5)]
    
myTray = Tray()
print(f"Tray contains {len(myTray.tray)} beakers")
del myTray
print("Tray has been deleted")
