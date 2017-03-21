import random
from switch import Switch

class Osob:
    
    fit=10000
    alive=0
    switchQuantity=0
    portNumber=Switch.portNumber
    portNumberGB=Switch.portNumGB
    
    def __init__(self, length):
        self.genom=[]
        for i in range(length):
            self.genom.append(random.randint(0,1)) 
