import networkx as nx 
import matplotlib.pyplot as plt
import math
import timeit
import time
 

    
 
print('Время старта =',time.perf_counter( ),'c' )

#loglinks=[]
#G. add_edge ( '1','2' ,5)

class PhLink:
    home=None
    end=None
    weight=1
l1=PhLink()
l2=PhLink()
l3=PhLink()


e=[l1,l2,l3]


print('ss', e[0].home)

class LgLink:
    home=None
    end=None
   
f1=LgLink()
f2=LgLink()
f3=LgLink()
b=[f1,f2,f3]
print('ss', b[0].home)

#while w < len
#
#f=nx.astar_path(G,w[y][0],w[y][1],heuristic=None,weight=2)

R=0

    
class Astar:
    loggraph = b
    def calc(self,osob):
        G=nx.DiGraph()
        r=0
        while r<len(osob.ph_link):
            G.add_edge(osob.ph_link[r].home,osob.ph_link[r].end)
            r+=r+1
        print(G)
        
        m=0
        i=0
        j=0
        print(self.loggraph)
        
        while m<(len(self.loggraph)):
            y=str(self.loggraph[m].home)
            z=str(self.loggraph[m].end)
            f=nx.astar_path(G,y,z,heuristic=None,weight='weight')
            print('m=',m)
            print(f)
            m=m+1
            while i<(len(f)-1): # Анализируем ребра 
                while j<(len(osob.ph_link)): #Находим iое ребро в списке e
                    if osob.ph_link[j].home==f[i] and osob.ph_link[j].end==f[i+1]: 
                        print('x=',osob.ph_link[j].weight+1)
                        tmp = list(osob.ph_link[j])
                        tmp[2]=tmp[2]+1
                        osob.ph_link[j]=tuple(tmp)
                        G.add_edge(osob.ph_link[j].home,osob.ph_link[j].end)
                    j=j+1
                i=i+1
                j=0
            i=0
        k=0
        W=0
        R=0
        while k<(len(osob.ph_link)):
            if osob.ph_link[k].weight>5:
                W+=100*math.fabs(osob.ph_link[k].weight-5)
            if osob.ph_link[k].weight==1:
                W+=100*math.fabs(osob.ph_link[k].weight-5)
                
            k=k+1
            print(k)
        print('W=',W)
        print('R=', R)
        
    def update(self):
       # G.add_weighted_edges_from(self.phgraph)
       # print(self.phgraph)
#print('Время завершения =',time.perf_counter( ),'c' )
#Return the value (in fractional seconds) of a performance counter,
#i.e. a clock with the highest available resolution to measure a short duration.
#It does include time elapsed during sleep and is system-wide. The reference point of the returned
#value is undefined, so that only the difference between the results of consecutive calls is valid.
#print('Время c учетом производительности =',time.process_time( ),'c')
#Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process. 

obj1 = Astar()
print (obj1.loggraph)

obj1.calc()
#obj1.update()








