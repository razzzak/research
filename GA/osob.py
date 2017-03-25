import random
from switch import Switch
from physical_link import Physical_link

class Osob:
    
    fit=10000
    alive=0
    switchQuantity=0
    portNumber=Switch.portNumber
    portNumberGB=Switch.portNumGB
    ph_link=[]
    
    def __init__(self, length):
        self.genom=[]
        for i in range(length):
            self.genom.append(random.randint(0,1)) 
