class Physical_link:
    home= None
    end= None
    weight=1
    def __init__(self):
        self.log_s=set()
    def getEdge(self):
        return (self.home, self.end)
