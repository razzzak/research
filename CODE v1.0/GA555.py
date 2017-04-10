import random
from osob import Osob 
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

        self.fitness_functions=[GenAlg.fitness1, GenAlg.fitness2, GenAlg.fitness3, GenAlg.fitness4, GenAlg.fitness5]
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
        plt.xlim(-50,1000)
        plt.ylim(-50,600)
        #plt.show()


        for i in range(1000):
            self.fitness(self.population[i])

        self.population.sort(key=lambda Osob: Osob.fit)
        while len(self.population)>100: 
            del self.population[100]

        self.bestOsob.fit=5000
        self.bestOsob.genom=[]

        for osob in self.population:
            self.ph_links(osob)
            osob.fit=10000

        self.bestOsob_alive3=0
        while self.bestOsob_alive3 < 1:
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
        print (self.bestOsob.fit)
        self.ph_links(self.bestOsob)
        self.fitnessAstar(self.bestOsob)
        self.draw_graph(self.bestOsob)
        
        #визуализация
    def draw_graph(self, osob):
        G=nx.Graph() #граф физ связей
        F=nx.Graph() #граф лог связей
        colors = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'purple', 'red','yellow','brown']
        #for edge in osob.ph_link+self.Log_Con:
        graph_pos={}
        weights_ph=[]
        colorss_ph=[]
        MUs=[]
        Terms=[]
        Switches=[]
        for phl in osob.ph_link:
            G.add_edge(phl.home.name, phl.end.name, weight=(phl.weight*1.0))
            graph_pos[phl.home.name]=[phl.home.coords.x,phl.home.coords.y]
            graph_pos[phl.end.name]=[phl.end.coords.x,phl.end.coords.y]
            colorss_ph.append(random.choice(colors))
            weights_ph.append(phl.weight*1.0*5.0)
            phl.weight=1
        for mu1 in self.MU:
            MUs.append(mu1.name)
        for term1 in self.Terminal:
            Terms.append(term1.name)
        for sw in self.Switch:
            Switches.append(sw.name)
                
        #for i in weights_ph:
         #   print (i)
          
        #dobavim Astar
        graphp_pos={}
        flows=[]
        edges=[]
        colorss=[]
        weights=[]
        for log in self.Log_Con:
            log_h=log.home.name
            log_e=log.end.name
            f = nx.astar_path(G,log_h,log_e)
            flows.append(f)
            G.add_path([f])
            colorss.append(random.choice(colors))
            for link in range (1, len(f)-1):
                colorss.append(colorss[-1])
        Fl=nx.Graph()
        for f in flows:
            print (f)
            for n in range (len(f)-1):
                route_edges=[(f[n],f[n+1])]
                Fl.add_nodes_from(f)
                Fl.add_edges_from(route_edges)
                edges.append(route_edges)
            print("Graph has %d nodes with %d edges" %(Fl.number_of_nodes(),
                                                           Fl.number_of_edges()))
        #for f in colorss:
         #   print (f)
            
        for edge in self.Log_Con:
            F.add_edge(edge.home.name, edge.end.name)
        #создадим координаты для логических связей
        graphlog_pos={}
        for item in self.Log_Con:
            graphlog_pos[item.home.name]=[item.home.coords.x+1,item.home.coords.y+1]
            graphlog_pos[item.end.name]=[item.end.coords.x+1,item.end.coords.y+1]
        #print (graphlog_pos)
        #nx.draw_networkx_edges(G, graph_pos, width=weights_ph, edge_color=colorss_ph)
        # нарисуем потоки в соотв с Астар
        
        for ctr, edgelist in enumerate(edges):   
            nx.draw_networkx_edges(Fl, graph_pos, edgelist=edgelist, width=3, edge_color=colorss[ctr])
        # нарисуем физ.связи
        #nx.draw_networkx_edges(G, graph_pos, edgelist=graph, edge_size=5, edge_color='black') 
        #nx.draw_networkx_edges(G, graph_pos, edgelist=graphlog, edge_size=5, edge_color='yellow')
        #nx.draw_networkx_nodes(G, graph_pos,  node_size=500, node_color='red', alpha=1.0)
        nx.draw_networkx_edges(F, graphlog_pos, edge_size=10, edge_color='black', style='dashed')
        nx.draw_networkx_nodes(G, graph_pos, nodelist=MUs, node_size=800, node_color='red', node_shape='h', alpha=1.0)
        nx.draw_networkx_nodes(G, graph_pos, nodelist=Terms, node_size=800, node_color='green', node_shape='o', alpha=1.0) 
        nx.draw_networkx_nodes(G, graph_pos, nodelist=Switches, node_size=800, node_color='orange', node_shape='s', alpha=1.0) 
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
                    phl.home=switch1
                    phl.end=self.Switch[i]
                    osob.ph_link.append(phl)
                else:
                    continue
            for i in range(n,len(genPart1)):
                if genPart1[i]>0:
                    phl=Physical_link()
                    phl.home=switch1
                    phl.end=self.Switch[(i+1)]
                    osob.ph_link.append(phl)
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
        else:
            osob.fit+=10000
        osob.fit+=self.fitness4(g)
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
            if u<1:
                f3+=9998
            else:
                f3+=0
        return f3

    def fitness4(self, genom): #ff4 минимизирование физ связей
        f4=0
        counter=0
        device_amount=(len(self.IED)+len(self.Switch)-1)
        for link in genom:
            if link==1:
                counter+=1
            else:
                continue 
        if counter>device_amount:
            f4+= 11*(counter-device_amount)
        else:
            f4+=0
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
        G=nx.Graph()
        for phl in osob.ph_link:
            phl.weight=1
            G.add_edge(phl.home.name, phl.end.name, weight = phl.weight)
        for log in self.Log_Con:
            log_h=log.home.name
            log_e=log.end.name
            try:
                f = nx.astar_path(G,log_h,log_e)
            except:
                print(f)
            if nx.has_path(G,log_h,log_e)==True:
                for link in range (0, len(f)-1): # Анализируем ребра
                    for phl in osob.ph_link: # проверка на наличие
                        if phl.home.name==f[link] and phl.end.name==f[link+1]:
                            if isinstance(phl.home,Switch)  and isinstance(phl.end,Switch):
                                phl.weight+=((phl.weight*5)+1)*0.2
                                G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
                            else:
                                phl.weight+=1
                                G.edge[phl.home.name][phl.end.name]['weight'] = phl.weight
            elif nx.has_path(G,log_h,log_e)==False:
                W+=10000
        for phl in osob.ph_link:
            if phl.weight>5:
                W+=100*math.fabs(phl.weight-5)
            if phl.weight==1:
                W+=301*math.fabs(phl.weight)
        return W


    def cross(self, good_pop, bad_old_osob): #скрещивание
        s = len(good_pop)
        osob_1 = good_pop[random.randint(0,(len(good_pop)-1))]
        good_pop2=good_pop[:]
        good_pop2.remove(osob_1)
        osob_2 = good_pop2[random.randint(0,(len(good_pop2)-1))]
        bad_old_osob.genom=osob_1.genom[:]
        d=random.randint(2,4) #выбор кол-ва скрещиваемых генов
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
