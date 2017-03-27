import networkx as nx 
import matplotlib.pyplot as plt
G=nx.DiGraph()

e=[('1','5',3),('2','5',2),('3','5',1),('5','7',1),('4','6',1),('7','8',13),('6','9',1)]

k=list(e)
print(k)
print(e[0][1])
G.add_weighted_edges_from(e)
#loglinks=[]
#G. add_edge ( '1','2' ,5)
print(e)
print(len(e))
#G[1][2]['weight'] = 4.7
#G.edge[1][2]['weight'] = 4
#def heuristic(a,b):  
 #   return 0
print(nx.astar_path_length(G,'1','8',heuristic=None,weight=2))
print(nx.astar_path_length(G,'3','5',heuristic=None,weight=5 ))
print(nx.astar_path_length(G,'4','9',heuristic=None,weight='wes' ))
print(nx.astar_path(G,'1','8',heuristic=None,weight=2))

nx.draw(G)
plt.savefig("path.png")

class PhLink:
    home=None
    end=None
    wes=0
#l1=PhLink()
#l2=PhLink()
#l3=PhLink()
#e=[l1,l2,l3]
print()
#while w < len
#
#f=nx.astar_path(G,w[y][0],w[y][1],heuristic=None,weight=2)

f=nx.astar_path(G,'1','8',heuristic=None,weight=2)



i=0
j=0

while i<(len(f)-1): # Анализируем ребра 
    while j<(len(e)-1): #Находим iое ребро в списке e
       if e[j][0]==f[i] and e[j][1]==f[i+1]: 
            print('x=',e[j][2]+1)
       j=j+1
       print(j)
       print()
    
    i=i+1
    j=0
print(i)
print(e)
    

#for n,nbrsdict in G.adjacency_iter():
     #for nbr,eattr in nbrsdict.items():
      #  if 'weight' in eattr:
       #   print((n,nbr,eattr['weight']))
        #if DiGraph.has_edge(n, nbrsdict) True
            #то изменяем вес в графе e
       # else print("Путь не найден")
#G.edges(data='weight')

#while 
    #if DiGraph.has_edge(U, V) True #Возвращает истину, если ребро (и, v) в графе.
       # G.edge[1][2]['weight'] = 4
        #else print("Путь не найден")

