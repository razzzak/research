class Logical_conn:
    name= 'GOOSE'
    sv_num=5
    home= None
    end= None
    def __str__(self):
        return "Logical_conn from: %s to: %s"%(self.home , self.end)  
