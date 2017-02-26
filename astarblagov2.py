import networkx as nx 
import matplotlib.pyplot as plt
import math
import timeit
import time
 

 
print('Время старта =',time.perf_counter( ),'c' )
G=nx.DiGraph()

e=[('1','5',3),('1','3',1),('3','5',1),('5','7',1),('4','6',1),('7','8',1),('6','9',1)]

print(e)
G.add_weighted_edges_from(e)
#loglinks=[]
#G. add_edge ( '1','2' ,5)

#class PhLink:
#    home=None
#    end=None
#    wes=0
#l1=PhLink()
#l2=PhLink()
#l3=PhLink()
#e=[l1,l2,l3]
#print()
#while w < len
#
#f=nx.astar_path(G,w[y][0],w[y][1],heuristic=None,weight=2)



b=[(1,7),(1,8)]
m=0
i=0
j=0
print(b)
a=len(b)
print(a)
while m<(len(b)):
    y=str(b[m][0])
    z=str(b[m][1])
    f=nx.astar_path(G,y,z,heuristic=None,weight='weight')
    print('m=',m)
    print(f)
    m=m+1
    while i<(len(f)-1): # Анализируем ребра 
        while j<(len(e)-1): #Находим iое ребро в списке e
            if e[j][0]==f[i] and e[j][1]==f[i+1]: 
                print('x=',e[j][2]+1)
                tmp = list(e[j])
                tmp[2]=tmp[2]+1
                e[j]=tuple(tmp)
                G.add_weighted_edges_from(e)
            j=j+1
        i=i+1
        j=0
    i=0
print(e)
k=0
W=0
while k<(len(e)-1):
    if e[k][2]>5:
        W+=100*math.fabs(e[k][2]-5)
        print(W)
    k=k+1
print(W)
    

print('Время завершения =',time.perf_counter( ),'c' )
#Return the value (in fractional seconds) of a performance counter,
#i.e. a clock with the highest available resolution to measure a short duration.
#It does include time elapsed during sleep and is system-wide. The reference point of the returned
#value is undefined, so that only the difference between the results of consecutive calls is valid.
print('Время c учетом производительности =',time.process_time( ),'c')
#Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process. 

nx.draw(G)
plt.savefig("graf.png")

