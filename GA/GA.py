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
    def __init__(self, IED, Switch, Logical_conn):
        self.genom=[]
        self.IED=IED
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
        print(Switch[1].name)
        
        
        self.population = []

        # создание популяции
        for i in range (1000):  
            self.portNumber=Osob.portNumber
            self.switchQuantity=v
            self.population.append([])
            self.population[i]=Osob(len(self.genom))
            self.portNumberGB=Osob.portNumberGB
        
        self.bestOsob=Osob(len(self.genom))
        #self.bestOsob.genom=self.population[0].genom[:] #лучшая особь - первая особь популяции
        self.bestOsob_alive=0
        os_x=[]
        os_y=[]
        step=0

        self.fitness_functions=[GenAlg.fitness1, GenAlg.fitness2, GenAlg.fitness3]
        self.fitness_functions_3modul=[GenAlg.fitness1, GenAlg.fitness2, GenAlg.fitness3]

        while self.bestOsob_alive < 100: #основное тело 2 модуля: пока лучшая особь не останется лучшей 100 раз, алгоритм сортирует
            os_y.append(self.bestOsob.fit)
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
            bestNum=int((len(self.population))*0.2) #выбираем процент лучших особей, 
            best=self.population[0:(bestNum)]
            for osob in self.population[(bestNum):-1]:
                self.cross(best, osob)
            for osob in self.population[1:(bestNum)]:
                self.mutation(osob)
            step+=1
        plt.scatter (os_x,os_y)
        plt.xlim(0,150)
        plt.ylim(0,10500)
        #plt.show()

        #for osob in range(950,980):
         #   print(self.population[osob].fit)

        for i in range(1000):
            self.fitness(self.population[i])

        self.population.sort(key=lambda Osob: Osob.fit)
        while len(self.population)>100: #уменьшим популяцию до 100 особей
            del self.population[100]

        for osob in self.population:  #добавим оставшимся особям физические связи
            #print(osob.fit)
            self.ph_links(osob)
            osob.fit=10000
        #print (len(self.population[0].ph_link))
        #for j in range (len(self.population[0].ph_link)):
         #   print (self.population[0].ph_link[j].home.name)
          #  print (self.population[0].ph_link[j].end.name)
        #print (self.population[0].genom)

        self.bestOsob_alive3=0
        while self.bestOsob_alive3 < 100: #пока лучшая особь не останется лучшей 100 раз 
            for i in range(100):        #алгоритм работает с учетом третьего модуля
                self.fitness_3modul(self.population[i])
            self.population.sort(key=lambda Osob: Osob.fit)
            if self.bestOsob.genom!=self.population[0].genom: #счетчик алгоритма
                self.bestOsob.genom=self.population[0].genom[:]
                self.bestOsob.fit=self.population[0].fit
                self.bestOsob.ph_link=self.population[0].ph_link[:]
                self.bestOsob_alive3=0
            else:
                self.bestOsob_alive3 = self.bestOsob_alive3+1
            #print (self.population[8].fit)
            bestNum=int((len(self.population))*0.2) #выбираем процент лучших особей, 
            best=self.population[0:(bestNum)]
            for osob in self.population[(bestNum):-1]:
                #r=0
                #while r<len(osob.ph_link):
                 #   print(osob.ph_link[r].home.name)
                  #  print(osob.ph_link[r].end.name)
                   # r+=1
                #print (osob.genom)
                self.cross(best, osob)
                self.ph_links(osob)
                #r=0
                #while r<len(osob.ph_link):
                 #   print(osob.ph_link[r].home.name)
                  #  print(osob.ph_link[r].end.name)
                   # r+=1
                #print (osob.genom)
            for osob in self.population[1:(bestNum)]:
                self.mutation(osob)
                self.ph_links(osob)

        print (self.bestOsob.genom)
        r=0
        while r<len(self.bestOsob.ph_link):
            print(self.bestOsob.ph_link[r].home.name)
            print(self.bestOsob.ph_link[r].end.name)
            r+=1
        print (self.bestOsob.fit)
        self.ph_link=[]
        self.ph_links(self.bestOsob)
        #print (self.bestOsob.ph_link[0].home.name)
        #print (self.Ph_link)

        #return self.bestOsob
  

    def ph_links(self, osob): #определение физических связей
        osob.ph_link=[]
        for ied1 in self.IED:
            genPart = osob.genom[ied1.genStart:ied1.genEnd]
            for i in range(0,len(genPart)):
                if genPart[i]>0:
                    phl=Physical_link()
                    phl.home=ied1
                    phl.end=self.Switch[i]
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
        for f in self.fitness_functions:
            osob.fit = osob.fit + f(self, g)
        #print (osob.fit)
        if osob.fit<1:
            osob.fit+=self.fitnessAstar(osob)
        else:
            osob.fit+=10000
        return (osob.fit)


    def fitness1(self, genom): #первая фитнесс-функция. проверяет, чтобы все иеды имели хотя бы одно подкл-е
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
        
        
    def fitness2(self, genom): #2я фитнесс-функции. проверяет, чтобы кол-во занятых 
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


    def fitness3(self, genom): #3я фитнесс-функция: проверяет, чтобы кол-во занятых 1GB-портов
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
            if u<2:
                f3+=9998
            else:
                f3+=0
        return f3
    
            
    def fitnessAstar(self, osob): #здесь д.б. 3й модуль
        G=nx.Graph()
        r=0
        #print (osob.genom)
        while r<len(osob.ph_link):
            #print(osob.ph_link[r].home.name)
            #print(osob.ph_link[r].end.name)
            #print(r)
            G.add_edge((osob.ph_link[r].home.name),(osob.ph_link[r].end.name), weight = osob.ph_link[r].weight)
            osob.ph_link[r].weight=1
            r+=1
        #print(G)
            

        m=0
        i=0
        j=0
        
        while m<(len(self.Log_Con)):
            y=(self.Log_Con[m].home.name)
            z=(self.Log_Con[m].end.name)
            f=nx.astar_path(G,y,z,heuristic=None)
            #print('m=',m)
            #print(f)
            m=m+1
            while i<(len(f)-1): # Анализируем ребра 
                while j<(len(osob.ph_link)): #Находим iое ребро в списке e
                    if osob.ph_link[j].home==f[i] and osob.ph_link[j].end==f[i+1]: 
                        osob.ph_link[j].weight=(osob.ph_link[j].weight)+1
                        G.add_edge(osob.ph_link[j].home,osob.ph_link[j].end, weight = osob.ph_link[j].weight)
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
                W+=100*math.fabs(osob.ph_link[k].weight)
                
            k=k+1
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

        
        
