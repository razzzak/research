
from ied import Terminal
from ied import MU
from port import Port
from logical_conn import Logical_conn
from physical_conn import Physical_conn
from switch import Switch
import math
class XmlParser:
  
  #def buildIED (iedelem):
    #result = IED()
    #print(dir(iedelem))
    #result.name=iedelem.get("name")
    #print(result)
    #return result

  def buildSwitch (self, switchelem):
    result = Switch()
    #print(dir(iedelem))
    result.name=switchelem.get("name")
    #print(result)
    return result


  def buildMU (self, muelem):
    result = MU()
    #print(dir(muelem))
    for child in muelem:
      if child.tag=="name":
        result.name=child.text
    #print(result)
    return result

  def buildTerminal (self, iedelem):
    result = Terminal()
    #print(dir(ied1elem))
    for child in iedelem:
      if child.tag=="name":
        result.name=child.text 
      if child.tag=="model":
        result.model=child.text
      if child.tag=="ports":
        g=int(child.text)
        #print(g)
    result.ports=[]
    for i in range (g):
      i=Port()
      result.ports.append(i)
          
    
    #print(result)
    #print(result.model)
    #print(len(result.ports))
    return result

  def buildPort (self, portelem):
    result = Port()
    #print(dir(iedelem))
    result.name=portelem.get("name")
    #print(result)
    return result

  def buildLogical_conn (self, logical_connelem):
    result = Logical_conn()
    all_i=self.MUs+self.Terminals
    
    mu_name=logical_connelem.get("home")
    for t in all_i:
      for child in logical_connelem:
        if child.tag=="home":
          if t.name==child.text:
            result.home=t
            break
    Terminal_name=logical_connelem.get("end")
    for p in all_i:
      for child in logical_connelem:
        if child.tag=="end":
          if p.name==child.text:
            result.end=p
            break
    for child in logical_connelem:
      if child.tag=="sv_num":
        result.sv_num=int(child.text)
     
    print(result.sv_num)
    print(result.end.name)
    #print(dir(iedelem))
    #print(result)
    return result

  def parser(self):
    pass
  def __init__(self, filename):  
    self.Terminals=[]
    self.MUs=[]
    self.Ports=[]
    self.Logical_conns=[]
    self.Switchs=[]
    #all_i=[]
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    for iedelem in root.iter("Terminal"):
      ied=self.buildTerminal(iedelem)
      self.Terminals.append(ied)
      
    for switchelem in root.iter("Switch"):
      pass
      #switch=buildSwitch(switchelem)
      #Switchs.append(switch)
    #for i in Switchs:
      #print (i.ports)
    for muelem in root.iter("MU"):
      mu=self.buildMU(muelem)
      self.MUs.append(mu)

    for portelem in root.iter("Port"):
      port=self.buildPort(portelem)
      self.Ports.append(port)

    for logical_connelem in root.iter("Logical_conn"):
      logical_conn=self.buildLogical_conn(logical_connelem)
      self.Logical_conns.append(logical_conn)
      
    #for i in Terminals:
      #print (len(i.ports))




    #округлить в большую сторону
    sw_number=(math.ceil(((len(self.Terminals)*1)+(len(self.MUs)*1))/(Switch.portNumber-4)*1.5))
    #print(sw_number)
    for i in range (sw_number):
      h=Switch()
      #print(h.name)
      self.Switchs.append(h)
    #print (len(self.Switchs))

    a=set()
    for MU in self.MUs:
      MU.summ=set()
      for logical_conn in self.Logical_conns:
        if MU.name==logical_conn.home.name:
          MU.summ.add(logical_conn.end.name)
    #for MU in self.MUs:
      #print(set(MU.summ))   





