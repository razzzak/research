import unittest
from xmlparser import XmlParser

class TestStringMethods(unittest.TestCase):

  def test1(self):
      x=XmlParser("new1.xml")
      self.assertTrue(x!=None)

  def test2(self):
      x=XmlParser("new1.xml")
      self.assertTrue(len(x.MUs)>0)
      self.assertTrue(len(x.Terminals)>0)
      self.assertTrue(len(x.Ports)>0)
      self.assertTrue(len(x.Logical_conns)>0)
      self.assertTrue(len(x.Switchs)>0)
  
if __name__ == '__main__':
    unittest.main()

    #def test3(self):
      #for MU in self.MUs:
        
        #print(set(summ))
