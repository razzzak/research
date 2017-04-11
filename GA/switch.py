from gen import Gen
from ied import Coords

class Switch(Gen):
    name= 'ur'
    portNumber = 24
    portNumGB = 8
    ports=[]
    coords=Coords(0,350)
    count=0
    def __init__(self):
        self.coords = Coords(Switch.coords.x,Switch.coords.y)
        Switch.coords.x+=200
        Switch.count+=1;
        self.name="ur%i"%Switch.count
    def __str__(self):
       return "Switch%s"%self.name
