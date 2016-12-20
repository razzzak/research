import re

class IED(object):
    def __init__(self, _id, ports=None):
        self.id = _id
        self.ports = ports


class MU(object):
    def __init__(self, _id, ports=None):
        self.id = _id
        self.ports = ports

f = open('C:\\Python27\\rd.xml')
text = f.read()
ieds = re.findall('<IED.*?>(IED_\d+).*?<ports>(.*?)</ports>.*?</IED.*?>', text, re.DOTALL)
mus = re.findall('<MU.*?>(MU_\d+).*?<ports>(.*?)</ports>.*?</MU.*?>', text, re.DOTALL)

objs_ied = [IED(_id, int(ports)) for _id, ports in ieds]
objs_mu = [MU(_id, int(ports)) for _id, ports in mus]

