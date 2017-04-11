import random
from osob import Osob 
from ied import IED 
from switch import Switch
from port import Port
from physical_link import Physical_link
import networkx as nx
import math
import timeit
import time
from logical_conn import Logical_conn
import matplotlib as mpl
import matplotlib.pyplot as plt 
    

class GenAlg:
    
    def run(self):
        pass
    
    #создание генома
    def __init__(self, MU, Terminal, Switch, Logical_conn):
        self.genom=[]
        self.MU=MU
        self.Terminal=Terminal
        self.IED=self.MU+self.Terminal
        self.Switch = Switch
        self.Log_Con=Logical_conn
        v = len(self.Switch)
        #print (v)
        for i in self.IED:
            i.genStart=(len(self.genom))
            for j in self.Switch:
                self.genom.append(1)
            else:
                i.genEnd=(len(self.genom))
                
        for i in self.Switch:
            i.genStart=(len(self.genom))
            for j in self.Switch:
                if j !=i:
                    self.genom.append(1)
                else:
                    continue
            else:
                i.genEnd=(len(self.genom))
        print(Switch[0].name)
        
        
        self.population = []

        # создание популяции
        for i in range (1000):  
            self.portNumber=Osob.portNumber
            self.switchQuantity=v
            self.population.append([])
            self.population[i]=Osob(len(self.genom))
            self.portNumberGB=Osob.portNumberGB
        
        self.bestOsob=Osob(len(self.genom)) 
        self.bestOsob_alive=0
        os_x=[]
        os_y=[]
        step=0

        self.fitness_functions=[GenAlg.fitness1, GenAlg.fitness2, GenAlg.fitness3, GenAlg.fitness5]
        self.fitness_functions_3modul=[GenAlg.fitness1, GenAlg.fitness2, GenAlg.fitness3, GenAlg.fitness5]

        while self.bestOsob_alive < 100: #основное тело 2 модуля: пока лучшая особь 
            os_y.append(self.bestOsob.fit) #не останется лучшей 100 раз, алгоритм сортирует
            os_x.append(step)
            for i in range(1000):
                self.fitness(self.population[i])
            #сортировка!!!
            self.population.sort(key=lambda Osob: Osob.fit)
            if self.bestOsob.genom!=self.population[0].genom: #счетчик алгоритма
                self.bestOsob.genom=self.population[0].genom[:]
                self.bestOsob.fit=self.population[0].fit
                self.bestOsob_alive=0
            else:
                self.bestOsob_alive = self.bestOsob_alive+1
            bestNum=int((len(self.population))*0.2) #выбираем процент лучших особей
            best=self.population[0:(bestNum)]
            for osob in self.population[(bestNum):-1]:
                self.cross(best, osob)
            for osob in self.population[1:(bestNum)]:
                self.mutation(osob)
            step+=1
        #plt.scatter (os_x,os_y)
        plt.xlim(-100,1000)
        plt.ylim(-50,800)
        #plt.show()


        for i in range(1000):
            self.fitness(self.population[i])

        self.population.sort(key=lambda Osob: Osob.fit)
        while len(self.population)>100: 
            del self.population[100]

        self.bestOsob.fit=15000
        self.bestOsob.genom=[]

        for osob in self.population:
            self.ph_links(osob)
            osob.fit=10000

        self.bestOsob_alive3=0
        #while self.bestOsob_alive3 <100 and self.bestOsob.fit!=len(self.bestOsob.ph_link):
        #while self.bestOsob.fit>3000:
        while self.bestOsob_alive3 <100:
            for i in range(0,100):       
                self.fitness_3modul(self.population[i])
            self.population.sort(key=lambda Osob: Osob.fit)
            if self.bestOsob.genom!=self.population[0].genom:
                self.bestOsob.genom=self.population[0].genom[:]
                self.bestOsob.fit=self.population[0].fit
                self.bestOsob.ph_link=self.population[0].ph_link[:]
                self.bestOsob_alive3=0
            else:
                self.bestOsob_alive3 = self.bestOsob_alive3+1
            bestNum=int((len(self.population))*0.2)
            best=self.population[0:(bestNum)]
            for osob in self.population[(bestNum):-1]:
                self.cross(best, osob)
                self.ph_links(osob)
            for osob in self.population[1:(bestNum)]:
                self.mutation(osob)
                self.ph_links(osob)

        print (self.bestOsob.genom)
        counter=0
        for i in self.bestOsob.genom:
            if i==1:
                counter+=1
            else:
                continue
        print('ya counter=%s'%counter)
        print (self.bestOsob.fit)
        self.ph_links(self.bestOsob)
        self.fitnessAstar(self.bestOsob)
        self.draw_graph(self.bestOsob.ph_link)
        
        #визуализация
    def draw_graph(self, links):
        G=nx.DiGraph() #граф физ связей
        F=nx.Graph() #граф лог связей
        colors = ['#800000','#8B0000','#A52A2A','#B22222','#DC143C','#FF0000','#FF6347','#FF7F50',
                  '#CD5C5C','#F08080','#E9967A','#FA8072','#FFA07A','#FF4500','#FF8C00','#FFA500',
                  '#FFD700','#B8860B','#DAA520','#BDB76B','#808000','#FFFF00','#9ACD32','#556B2F',
                  '#6B8E23','#7CFC00','#7FFF00','#ADFF2F','#006400','#008000','#228B22','#00FF00',
                  '#32CD32','#90EE90','#98FB98','#8FBC8F','#00FA9A','#00FF7F','#2E8B57','#66CDAA',
                  '#3CB371','#20B2AA','#2F4F4F','#008080','#008B8B','#00FFFF','#00CED1','#40E0D0',
                  '#48D1CC','#7FFFD4','#B0E0E6','#5F9EA0','#4682B4','#6495ED','#00BFFF','#1E90FF',
                  '#87CEEB','#87CEFA','#191970','#000080','#00008B','#0000CD','#0000FF','#4169E1',
                  '#8A2BE2','#4B0082','#483D8B','#6A5ACD','#7B68EE','#9370DB','#8B008B','#9400D3',
                  '#9932CC','#BA55D3','#800080','#DDA0DD','#EE82EE','#FF00FF','#DA70D6','#C71585',
                  '#DB7093','#FF1493','#FF69B4','#FFB6C1','#FFC0CB','#8B4513','#A0522D','#D2691E',
                  '#CD853F','#F4A460','#DEB887','#BC8F8F','#708090','#B0C4DE']
        graph_pos={}
        weights_ph=[]
        colorss_ph=[]
        MUs=[]
        Terms=[]
        Switches=[]
        for phl in links:
            G.add_edge(phl.home.name, phl.end.name, weight=(phl.weight*1.0))
            graph_pos[phl.home.name]=[phl.home.coords.x,phl.home.coords.y]
            graph_pos[phl.end.name]=[phl.end.coords.x,phl.end.coords.y]
            colorss_ph.append(random.choice(colors))
            weights_ph.append(phl.weight*1.0*2.0)
            phl.weight=1
        for mu1 in self.MU:
            MUs.append(mu1.name)
        for term1 in self.Terminal:
            Terms.append(term1.name)
        for sw in self.Switch:
            Switches.append(sw.name)          
        #dobavim Astar
        flows=[]
        edges=[]
        colorss=[]
        weights=[]
        grap=[]
        r=5
        # нарисуем физ.связи
        #nx.draw_networkx_edges(G, graph_pos, width=weights_ph, edge_color='black')       
        for log in self.Log_Con:
            log_h=log.home.name
            log_e=log.end.name
            f = nx.astar_path(G,log_h,log_e)
            flows.append(f)
            G.add_path([f])     
        dtx=2
        dty=2
        for f_num,f in enumerate(flows):
            Fl=nx.Graph()
            edges=[]
            colorss=[]
            colorss.append(random.choice(colors))
            for n in range (len(f)-2):
                colorss.append(colorss[-1])
            for n in range (len(f)-1):
                route_edges=(f[n],f[n+1])  
                edges.append(route_edges)
            print(f)
            Fl.add_edges_from(edges)
            Fl.add_nodes_from(f)
            print("Graph has %d nodes with %d edges" %(Fl.number_of_nodes(),Fl.number_of_edges()))
            #dtx=r*math.sin(f_num*(2*math.pi/len(flows))) 
            #dty=r*math.cos(f_num*(2*math.pi/len(flows)))
            dtx+=1
            dty+=1
            #print(dty)
            graphp_pos={}
            # нарисуем потоки в соотв с Астар
            for item in links:
                if isinstance(item.home,Switch) and isinstance(item.end,Switch):
                    graphp_pos[item.home.name]=[item.home.coords.x,item.home.coords.y-60+dty]
                    graphp_pos[item.end.name]=[item.end.coords.x,item.end.coords.y-60+dty]
                else:
                    graphp_pos[item.home.name]=[item.home.coords.x,item.home.coords.y]
                    graphp_pos[item.end.name]=[item.end.coords.x,item.end.coords.y]
            nx.draw_networkx_edges(Fl, graphp_pos, edgelist=edges, width=2, edge_color=colorss)   
        for edge in self.Log_Con:
            F.add_edge(edge.home.name, edge.end.name)
        #создадим координаты для логических связей
        graphlog_pos={}
        for item in self.Log_Con:
            graphlog_pos[item.home.name]=[item.home.coords.x+1,item.home.coords.y+1]
            graphlog_pos[item.end.name]=[item.end.coords.x+1,item.end.coords.y+1]
        #nx.draw_networkx_edges(G, graph_pos, edgelist=graph, edge_size=5, edge_color='black') 
        #nx.draw_networkx_edges(G, graph_pos, edgelist=graphlog, edge_size=5, edge_color='yellow')
        #nx.draw_networkx_nodes(G, graph_pos,  node_size=500, node_color='red', alpha=1.0)
        #nx.draw_networkx_edges(F, graphlog_pos, edge_size=10, edge_color='black', style='dashed')
        nx.draw_networkx_nodes(G, graph_pos, nodelist=MUs, node_size=1000, node_color='red', node_shape='h', alpha=1.0)
        nx.draw_networkx_nodes(G, graph_pos, nodelist=Terms, node_size=1000, node_color='blue', node_shape='o', alpha=1.0) 
        nx.draw_networkx_nodes(G, graph_pos, nodelist=Switches, node_size=4000, node_color='green', node_shape='s', alpha=1.0) 
        nx.draw_networkx_labels(G, graph_pos, font_size=8, font_family='sans-serif')
        plt.show()

        

    def ph_links(self, osob): #определение физических связей
        osob.ph_link=[]
        for mu1 in self.MU:
            genPart = osob.genom[mu1.genStart:mu1.genEnd]
            for i in range(0,len(genPart)):
                if genPart[i]>0:
                    phl=Physical_link()
                    phl.home=mu1
                    phl.end=self.Switch[i]
                    osob.ph_link.append(phl)
                else:
                    continue
        for term1 in self.Terminal:
            genPart = osob.genom[term1.genStart:term1.genEnd]
            for i in range(0,len(genPart)):
                if genPart[i]>0:
                    phl=Physical_link()
                    phl.home=self.Switch[i]
                    phl.end=term1
                    osob.ph_link.append(phl)
                else:
                    continue
        for switch1 in self.Switch:
            n=self.Switch.index(switch1)
            genPart1 = osob.genom[switch1.genStart:switch1.genEnd]
            for i in range(0,n):
                if genPart1[i]>0:
                    phl=Physical_link()
                    phl1=Physical_link()
                    phl.home=switch1
                    phl1.end=switch1
                    phl.end=self.Switch[i]
                    phl1.home=self.Switch[i]
                    osob.ph_link.append(phl)
                    osob.ph_link.append(phl1)
                else:
                    continue
            for i in range(n,len(genPart1)):
                if genPart1[i]>0:
                    phl=Physical_link()
                    phl1=Physical_link()
                    phl.home=switch1
                    phl1.end=switch1
                    phl.end=self.Switch[(i+1)]
                    phl1.home=self.Switch[(i+1)]
                    osob.ph_link.append(phl)
                    osob.ph_link.append(phl1)
                else:
                    continue
        return osob
    
                
    def fitness(self, osob): #подсчет фитнесс-функции
        g = osob.genom
        osob.fit=0
        for f in self.fitness_functions:
            osob.fit = osob.fit + f(self, g)
        return (osob.fit)

    def fitness_3modul(self, osob): #подсчет фитнесс-функции с учетом 3 модуля
        g = osob.genom
        osob.fit=0
        for f in self.fitness_functions_3modul:
            osob.fit = osob.fit + f(self, g)
        if osob.fit==0:
            osob.fit+=self.fitnessAstar(osob)
            osob.fit+=self.fitness4(g)
        else:
            osob.fit+=100000
        return (osob.fit)


    def fitness1(self, genom): #1ff: проверяет, чтобы все иеды имели хотя бы одно подкл-е
        f1=0
        for ied1 in self.IED:
            h=0
            genPart = genom[ied1.genStart:ied1.genEnd]
            for gen in genPart:
                if gen>0:
                    h += 1
            if h==0:
                f1+=3500
            else:
                f1+=0
                
        return f1
        
        
    def fitness2(self, genom): #ff2: проверяет, чтобы кол-во занятых 
        f2=0                   #100MB портов свитчей не превышало кол-во портов имеющихся
        for i in range (self.switchQuantity):
            p=0
            for ied1 in self.IED:
                genPart = genom[ied1.genStart:ied1.genEnd]
                if genPart[i-1]>0:
                    p += 1
                else:
                    continue
            if p>(self.portNumber):
                f2+=((p-self.portNumber)*1002)
            else:
                f2+=0
        return f2


    def fitness3(self, genom): #ff3: проверяет, чтобы кол-во занятых 1GB-портов
        f3=0                   #не превышало портов имеющихся, а также,  чтобы каждый свитч
        for switch1 in self.Switch:   #имел хоть одну связь с другим   
            u=0
            n=self.Switch.index(switch1)
            genPart = genom[switch1.genStart:switch1.genEnd]
            for i in genPart:
                if i>0:
                    u+=1
                else:
                    continue
            copySwitch=[]
            copySwitch=self.Switch[:]
            copySwitch.remove(switch1)
            for switches in copySwitch[0:n]:
                genPart = genom[switches.genStart:switches.genEnd]
                if (genPart[n-1])>0:
                    u+=1
                else:
                    continue
            for switches in copySwitch[n:(len(copySwitch))]:
                genPart1 = genom[switches.genStart:switches.genEnd]
                if genPart1[n]>0:
                    u+=1
                else:
                    continue
            if u>(self.portNumberGB):
                f3+=(u-self.portNumberGB)*1003
            else:
                f3+=0
            #if u<((len(self.Switch))-2):
            if u<1:
                f3+=9998
            else:
                f3+=0
        return f3

    def fitness4(self, genom): #ff4 минимизирование физ связей
        f4=0
        counter=0
        #device_amount=(len(self.IED)+len(self.Switch)-1)
        for link in genom:
            if link==1:
                counter+=1
            else:
                continue
        f4+= 1*(counter)
        return f4

    def fitness5(self, genom): #ff5 проверка на наличие у свитча хотя бы одной связи с иед
        f5=0
        for i in range (self.switchQuantity):
            p=0
            for ied1 in self.IED:
                genPart = genom[ied1.genStart:ied1.genEnd]
                if genPart[i-1]>0:
                    p += 1
                else:
                    continue
            if p==0:
                f5+=7001
            else:
                f5+=0
        return f5
        
            
    def fitnessAstar(self, osob):
        W=0
        G=nx.DiGraph()
        for phl in osob.ph_link:
            phl.weight=1
            G.add_edge(phl.home.name, phl.end.name, weight = phl.weight)
        for log in self.Log_Con:
            log_h=log.home.name
            log_e=log.end.name
            try:
                f = nx.astar_path(G,log_h,log_e)
            except nx.NetworkXNoPath:
                W=10000
                return W
            if (len(f)-2)>4: #trebovanie k otsutstviyu zaderzhek pri pereda4e
                W+=9991
                return W
            for link in range (0, len(f)-1): # Анализируем ребра
                for phl in osob.ph_link: # проверка на наличие
                    if phl.home.name==f[link] and phl.end.name==f[link+1]:
                        if isinstance(phl.home,Switch)  and isinstance(phl.end,Switch):
                            phl.log_s.add (log_h)
                            if len (phl.log_s)<13:
                                phl.weight+=0.2
                                G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                            else:
                                phl.weight+=5
                                G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                        elif isinstance(phl.home,IED) and isinstance(phl.end,Switch):
                            if log_e in phl.log_s: #proverka na nali4ie dannoi svyazi v set()
                                phl.weight+=0 #esli est' - ni4ego ne menyaem
                                G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                            else: #esli net 
                                phl.log_s.add (log_e) #- dobavlyaem svyaz
                                if len(phl.log_s)>len(phl.home.summ): #sravnivaem s dolgenstvuyucshim mnozhestvom
                                    phl.weight+=10 #esli previshaet - dobavlyaem bolshoi ves
                                    G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                                else: # elsi net
                                    phl.weight+=0 #ni4ego ne dobavlyaem
                                    G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                        elif isinstance(phl.home,Switch)  and isinstance(phl.end,IED):
                            phl.log_s.add (log_h)
                            if len (phl.log_s)<6:
                                phl.weight+=0.4 #proveryaem svyazi Switch-Terminal i dobavlyaem ves
                                G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                            else:
                                phl.weight+=4
        copyG= G.copy()
        #m=len(list(nx.simple_cycles(copyG)))
        #print (list(nx.simple_cycles(copyG)))
        #print (m)
        for ring in (list(nx.simple_cycles(copyG))):
            if len(ring)>2:
                W+=(len(ring)-2)*700
            else:
                W+=0
        for phl in osob.ph_link:
            #print (phl.weight)
            #vot tut s4itaem shtraf!!!
            if phl.weight>5:
                W+=49*math.fabs(phl.weight-5)
            if phl.weight==1:
                W+=41*math.fabs(phl.weight)
            if phl.weight<=5 and phl.weight>1:
                W+=(30/(phl.weight))
            phl.log_s.clear()
        return W


    def cross(self, good_pop, bad_old_osob): #скрещивание
        s = len(good_pop)
        osob_1 = good_pop[random.randint(0,(len(good_pop)-1))]
        good_pop2=good_pop[:]
        good_pop2.remove(osob_1)
        osob_2 = good_pop2[random.randint(0,(len(good_pop2)-1))]
        bad_old_osob.genom=osob_1.genom[:]
        d=random.randint(6,10) #выбор кол-ва скрещиваемых генов
        h=random.randint(0,(len(osob_1.genom)-d))
        for b in range (h, (h+d)):
            if osob_1.genom[b]!=(osob_2.genom[b]):
                bad_old_osob.genom[b]=osob_2.genom[b]
            else:
                continue
        return bad_old_osob

    def mutation(self, osob): #мутация
        z=1
        while z<6:
            i=random.randint(0, (len(osob.genom)-1))
            if osob.genom[i]!=1:
                osob.genom[i]=1
            else:
                osob.genom[i]=0
            z+=1
        return osob 
