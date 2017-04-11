from gen import Gen
class IED:
    iedType = 'terminal'
    model = 'siemens'
    name = '7ut87-at1'
    ports = []
    functions = []


class Coords():
    def __init__(self, x,y):
        self.x = x
        self.y = y


class MU(IED):
    name = 'f1'
    summ=set()#mnozehstvo v kot zapisani vse log Terminal dlya kot trebuetsya
    ports = [] #information ot dannogo MU
    coords=Coords(0,0)
    count=0
    def __init__(self):
        self.coords = Coords(MU.coords.x, MU.coords.y)
        MU.coords.x+=20
        MU.count+=1;
        self.name=MU.count
    def __str__(self):
        return "%s"%self.name

class Terminal(IED):
    name = '7ut87-at1'
    ports = []
    functions = []
    coords=Coords(0,700)
    count=0
    def __init__(self):
        self.coords = Coords(Terminal.coords.x, Terminal.coords.y)
        Terminal.coords.x+=75
        Terminal.count+=1;
        self.name=Terminal.count
    def __str__(self):
        return "%s"%self.name


