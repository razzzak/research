class Port:
    num=0
    portType = 'copper'
    speed = 100
    device = None
    def __str__(self):
        return "Port%i"%self.num  
