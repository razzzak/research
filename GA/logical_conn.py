class Logical_conn:
    name= 'GOOSE'
    home= None
    end= None
    def __str__(self):
        return "Logical_conn from: %s to: %s"%(self.home , self.end)  
