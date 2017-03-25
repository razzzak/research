import unittest
from GA import GenAlg
from ied import IED 
from switch import Switch
from osob import Osob 
 
class TestUM(unittest.TestCase):
    genalg=None
    def setUp(self):
        ied=[IED(),IED(),IED(),IED(),IED()]
        switch=[Switch(), Switch(),Switch()]
        self.genalg = GenAlg(ied,switch)

    def test_genalg(self):
        result = self.genalg.run()

    def test_mut(self):
        osob = Osob(21)
        original = Osob(21)
        original.genom = osob.genom[:]
        self.genalg.mutation(osob)
        changeCount = 0
        for i in range(len(osob.genom)):
            if original.genom[i]!=osob.genom[i]:
                changeCount+=1
        print("Mutated %i genes"%(changeCount))
        assert(changeCount>0)

    def test_cross(self):
        osob_1=Osob(21)
        osob_2=Osob(21)
        osob_1x2=Osob(21)
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
        length=21
        osob=Osob(length)
        osob.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1]
        x=self.genalg.fitness1(osob.genom)
        print ("fitness1 = ")
        print (x)
        assert(x<1000)

        
    def test_fitness2(self):
        length=21
        osob1=Osob(length)
        osob1.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1]
        z=self.genalg.fitness2(osob1.genom)
        print ("fitness2 = ")
        print (z)
        assert(z<500)
        

    def test_fitness3(self):
        length=21
        osob3=Osob(length)
        osob3.genom=[1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1]
        y=self.genalg.fitness3(osob3.genom)
        print ("fitness3 = ")
        print (y)
        assert(y<2)


if __name__ == '__main__':
    unittest.main()
