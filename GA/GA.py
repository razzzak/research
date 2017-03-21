import random
from osob import Osob 
from ied import IED 
from switch import Switch
from port import Port
from physical_link import Physical_link
import matplotlib as mpl
import matplotlib.pyplot as plt
    

class GenAlg:
    
    def run(self):
        pass
    
    #создание генома
    def __init__(self, IED, Switch):
        self.genom=[]
        self.IED=IED
        self.Switch = Switch
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
        
        
        self.fitness_functions=[GenAlg.fitness1, GenAlg.fitness2, GenAlg.fitness3]
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

        while self.bestOsob_alive < 100: #основное тело алгоритма: пока лучшая особь не останется лучшей 100 раз, алгоритм сортирует
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
        print (self.bestOsob.genom)
        print (self.bestOsob.fit)
        plt.scatter (os_x,os_y)
        plt.xlim(0,150)
        plt.ylim(0,10500)
        plt.show()
        self.Ph_link=[]
        self.visualis(self.bestOsob.genom,self.Ph_link)
        #print (self.Ph_link)
  

    def visualis(self, genom, Ph_link):
        for ied1 in self.IED:
            genPart = genom[ied1.genStart:ied1.genEnd]
            for i in genPart:
                if i>0:
                    phl=Physical_link()
                    self.Ph_link.append(phl)
                    phl.home=ied1
                    phl.end=self.Switch[i]
                else:
                    continue
        for switch1 in self.Switch:
            n=self.Switch.index(switch1)
            genPart = genom[switch1.genStart:switch1.genEnd]
            for i in genPart[0:n]:
                if i>0:
                    phl=Physical_link()
                    self.Ph_link.append(phl)
                    phl.home=switch1
                    phl.end=self.Switch[i]
                else:
                    continue
            for i in genPart[n:(len(genPart))]:
                if i>0:
                    phl=Physical_link()
                    self.Ph_link.append(phl)
                    phl.home=switch1
                    phl.end=self.Switch[(i+1)]
                else:
                    continue
        return Ph_link
    
                

    def fitness(self, osob): #подсчет фитнесс-функции
        g = osob.genom
        osob.fit=0
        for f in self.fitness_functions:
            osob.fit = osob.fit + f(self, g)
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
                f1+=1000
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
            if u<1:
                f3+=9998
            else:
                f3+=0
        return f3
            
            
 

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

        return self.bestOsob
        
        
