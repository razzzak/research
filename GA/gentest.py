import unittest
from GA import GenAlg
from ied import IED 
from switch import Switch
from osob import Osob
from logical_conn import Logical_conn

ied1 = IED()
ied1.name='MU1'
ied2 = IED()
ied2.name='MU2'
ied3 = IED()
ied3.name='MU3'
ied4 = IED()
ied4.name='MU4'
ied5 = IED()
ied5.name='MU5'
ied6 = IED()
ied6.name='MU6'
ied7 = IED()
ied7.name='Terminal_1'
ied8 = IED()
ied8.name='Terminal_2'
ied9 = IED()
ied9.name='Terminal_3'
switch1=Switch()
switch1.name='ur1'
switch2=Switch()
switch2.name='ur2'

L_l1=Logical_conn()
L_l1.home=ied1
L_l1.end=ied7

L_l2=Logical_conn()
L_l2.home=ied2
L_l2.end=ied7

L_l3=Logical_conn()
L_l3.home=ied3
L_l3.end=ied8

L_l4=Logical_conn()
L_l4.home=ied4
L_l4.end=ied8

L_l5=Logical_conn()
L_l5.home=ied5
L_l5.end=ied9

L_l6=Logical_conn()
L_l6.home=ied6
L_l6.end=ied9

L_l7=Logical_conn()
L_l7.home=ied3
L_l7.end=ied9


class TestUM(unittest.TestCase):
    genalg=None
    def setUp(self):
        ied=[ied1,ied2,ied3,ied4,ied5,ied6,ied7,ied8,ied9]
        switch=[switch1, switch2]
        log_c=[L_l1,L_l2,L_l3,L_l4,L_l5,L_l6,L_l7]
        self.genalg = GenAlg(ied,switch,log_c)

    def test_genalg(self):
        result = self.genalg.run()

    def test_mut(self):
        osob = Osob(22)
        original = Osob(22)
        original.genom = osob.genom[:]
        self.genalg.mutation(osob)
        changeCount = 0
        for i in range(len(osob.genom)):
            if original.genom[i]!=osob.genom[i]:
                changeCount+=1
        print("Mutated %i genes"%(changeCount))
        assert(changeCount>0)

    def test_cross(self):
        osob_1=Osob(22)
        osob_2=Osob(22)
        osob_1x2=Osob(22)
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
        length=22
        osob=Osob(length)
        osob.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1]
        x=self.genalg.fitness1(osob.genom)
        print ("fitness1 = ")
        print (x)
        assert(x<1000)

        
    def test_fitness2(self):
        length=22
        osob1=Osob(length)
        osob1.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1]
        z=self.genalg.fitness2(osob1.genom)
        print ("fitness2 = ")
        print (z)
        assert(z<500)
        

    def test_fitness3(self):
        length=22
        osob3=Osob(length)
        osob3.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1]
        y=self.genalg.fitness3(osob3.genom)
        print ("fitness3 = ")
        print (y)
        assert(y<2)



if __name__ == '__main__':
    unittest.main()
