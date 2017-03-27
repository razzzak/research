
from ied1 import Terminal
from ied1 import MU
from port import Port
from logical_conn import Logical_conn
from physical_conn import Physical_conn

#def buildIED (iedelem):
  #result = IED()
  #print(dir(iedelem))
  #result.name=iedelem.get("name")
  #print(result)
  #return result


def buildMU (muelem):
  result = MU()
  #print(dir(muelem))
  for child in muelem:
    if child.tag=="name":
      result.name=child.text
  print(result)
  return result

def buildTerminal (ied1elem):
  result = Terminal()
  #print(dir(ied1elem))
  for child in ied1elem:
    if child.tag=="name":
      result.name=child.text
  
  print(result)
  return result

def buildPort (portelem):
  result = Port()
  #print(dir(iedelem))
  result.name=portelem.get("name")
  print(result)
  return result

def buildLogical_conn (logical_connelem):
  result = Logical_conn()
  all_i=MUs+Terminals
  
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
  #print(dir(iedelem))
  print(result)
  return result


Terminals=[]
MUs=[]
Ports=[]
Logical_conns=[]

#all_i=[]
import xml.etree.ElementTree as ET
tree = ET.parse('rd.xml')
root = tree.getroot()
for ied1elem in root.iter("Terminal"):
  ied1=buildTerminal(ied1elem)
  Terminals.append(ied1)

for muelem in root.iter("MU"):
  mu=buildMU(muelem)
  MUs.append(mu)

for portelem in root.iter("Port"):
  port=buildPort(portelem)
  Ports.append(port)

for logical_connelem in root.iter("Logical_conn"):
  logical_conn=buildLogical_conn(logical_connelem)
  Logical_conns.append(logical_conn)
for i in Terminals:
  print (i.ports)


from sw import Switch



#колличество портов(мю+терм) сумарное/20 
