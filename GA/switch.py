from gen import Gen
from ied import Coords

class Switch(Gen):
    name= 'ur1'
    portNumber = 24
    portNumGB = 8
    ports=[]
    coords=Coords(0,250)
    count=0
    def __init__(self):
        self.coords = Coords(Switch.coords.x,Switch.coords.y)
        Switch.coords.x+=20
        Switch.count+=1;
        self.name=Switch.count
#    def __str__(self):
 #       return "Switch%i"%self.name

