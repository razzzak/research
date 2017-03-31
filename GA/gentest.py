import unittest
from GA import GenAlg
from ied import IED, MU, Terminal 
from switch import Switch
from osob import Osob
from logical_conn import Logical_conn
from physical_link import Physical_link

mu1 = MU()
mu1.name='MU1'
mu2 = MU()
mu2.name='MU2'
mu3 = MU()
mu3.name='MU3'
mu4 = MU()
mu4.name='MU4'
mu5 = MU()
mu5.name='MU5'
mu6 = MU()
mu6.name='MU6'
terminal1 = Terminal()
terminal1.name='Terminal_1'
terminal2 = Terminal()
terminal2.name='Terminal_2'
terminal3 = Terminal()
terminal3.name='Terminal_3'
switch1=Switch()
switch1.name='ur1'
switch2=Switch()
switch2.name='ur2'

L_l1=Logical_conn()
L_l1.home=mu1
L_l1.end=terminal1

L_l2=Logical_conn()
L_l2.home=mu2
L_l2.end=terminal1

L_l3=Logical_conn()
L_l3.home=mu3
L_l3.end=terminal2

L_l4=Logical_conn()
L_l4.home=mu4
L_l4.end=terminal2

L_l5=Logical_conn()
L_l5.home=mu5
L_l5.end=terminal3

L_l6=Logical_conn()
L_l6.home=mu6
L_l6.end=terminal3

L_l7=Logical_conn()
L_l7.home=mu3
L_l7.end=terminal3


#описание физических связей
P_l1=Physical_link()
P_l1.home=mu1
P_l1.end=switch1

P_l2=Physical_link()
P_l2.home=mu2
P_l2.end=switch1

P_l3=Physical_link()
P_l3.home=mu3
P_l3.end=switch1

P_l4=Physical_link()
P_l4.home=mu4
P_l4.end=switch2

P_l5=Physical_link()
P_l5.home=mu5
P_l5.end=switch2

P_l6=Physical_link()
P_l6.home=mu6
P_l6.end=switch2

P_l7=Physical_link()
P_l7.home=terminal1
P_l7.end=switch1

P_l8=Physical_link()
P_l8.home=terminal2
P_l8.end=switch1

P_l9=Physical_link()
P_l9.home=terminal3
P_l9.end=switch2

P_l10=Physical_link()
P_l10.home=switch1
P_l10.end=switch2


class TestUM(unittest.TestCase):
    genalg=None
    def setUp(self):
        mu=[mu1,mu2,mu3,mu4,mu5,mu6]
        terminal=[terminal1,terminal2,terminal3]
        switch=[switch1, switch2]
        log_c=[L_l1,L_l2,L_l3,L_l4,L_l5,L_l6,L_l7]
        self.genalg = GenAlg(mu,terminal,switch,log_c)

    def test_genalg(self):
        result = self.genalg.run()

    def test_mut(self):
        osob = Osob(20)
        original = Osob(20)
        original.genom = osob.genom[:]
        self.genalg.mutation(osob)
        changeCount = 0
        for i in range(len(osob.genom)):
            if original.genom[i]!=osob.genom[i]:
                changeCount+=1
        print("Mutated %i genes"%(changeCount))
        assert(changeCount>0)

    def test_cross(self):
        osob_1=Osob(20)
        osob_2=Osob(20)
        osob_1x2=Osob(20)
        good_pop = [osob_1,osob_2]
        osob_1x2.genom = osob_1.genom[:]
        self.genalg.cross(good_pop,osob_1x2)
        changeCount_cross=0
        changeCount_cross2=0
        for i in range(len(osob_1.genom)):
            if osob_1x2.genom[i]!=osob_1.genom[i]:
                changeCount_cross+=1
            if osob_1x2.genom[i]!=osob_2.genom[i]:
                changeCount_cross2+=1
        print("%i genes are crossed with osob_1"%(changeCount_cross))
        print("%i genes are crossed with osob_2"%(changeCount_cross2))
        assert(changeCount_cross>=0 or changeCount_cross2>=0)
        assert(changeCount_cross<5 or changeCount_cross2<5)

    def test_fitness1(self):
        length=20
        osob=Osob(length)
        osob.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1]
        x=self.genalg.fitness1(osob.genom)
        print ("fitness1 = %s"%x)
        print (x)
        assert(x<1000)

        
    def test_fitness2(self):
        length=20
        osob1=Osob(length)
        osob1.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1]
        z=self.genalg.fitness2(osob1.genom)
        print ("fitness2 =%s"%z)
        assert(z<500)
        

    def test_fitness3(self):
        length=20
        osob3=Osob(length)
        osob3.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1]
        y=self.genalg.fitness3(osob3.genom)
        print ("fitness3 =%s"%y)
        assert(y<2)

    def test_fitness4(self):
        length=20
        osob3=Osob(length)
        osob3.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1]
        y=self.genalg.fitness4(osob3.genom)
        print ("fitness4 =%s"%y)
        assert(y==33)

    def test_fitness5(self):
        length=20
        osob5=Osob(length)
        osob5.genom=[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1]
        y=self.genalg.fitness5(osob5.genom)
        print ("fitness5 =%s"%y)
        assert(y==7001)

    def test_ph_links(self):
        length=20
        osob_phl=Osob(length)
        osob_phl.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1]
        g=self.genalg.ph_links(osob_phl)
        counter_phl_1=0
        for phl_1 in osob_phl.genom:
            if phl_1==1:
                counter_phl_1+=1
            else:
                continue
        counter_phl = len(osob_phl.ph_link)
        print (counter_phl)
        if counter_phl_1==counter_phl:
            tester=1
        else:
            tester=0
        print ("tester = %s"%tester)
        assert(tester>0)

    def test_fitnessAstar(self):
        length=20
        osob_Astar=Osob(length)
        osob_Astar.genom=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        osob_Astar.ph_link=[P_l1,P_l2,P_l3,P_l4,P_l5,P_l6,P_l7,P_l8,P_l9,P_l10]
        log_c=[L_l1,L_l2,L_l3,L_l4,L_l5,L_l6]
        astar=self.genalg.fitnessAstar(osob_Astar)
        print ("astar = %s"%astar)
        assert(astar==903)



if __name__ == '__main__':
    unittest.main()
