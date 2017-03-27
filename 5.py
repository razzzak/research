import re

class IED(object):
    def __init__(self, _id, ports=None):
        self.id = _id
        self.ports = ports


class MU(object):
    def __init__(self, _id, ports=None):
        self.id = _id
        self.ports = ports

class Logical_conn(object):
    def __init__(self, home, end):
        self.home = home
        self.end = end

f = open('C:\\Python27\\rd1.xml')
text = f.read()
ieds = re.findall('<IED.*?>(IED_\d+).*?<ports>(.*?)</ports>.*?</IED.*?>', text, re.DOTALL)
mus = re.findall('<MU.*?>(MU_\d+).*?<ports>(.*?)</ports>.*?</MU.*?>', text, re.DOTALL)
Logical_conn = re.findall('<Logical_conn.*?>(Logical_conn_\d+).*?<home>(.*?)</home>.*?<end>(.*?)</end.*?>', text, re.DOTALL)
objs_ied = [IED(_id, int(ports)) for _id, ports in ieds]
objs_mu = [MU(_id, int(ports)) for _id, ports in mus]
print(ieds)
print(mus)
print(Logical_conn)

#получить потоки с иедов. добавить датастрим как логическую сущность. у иедов есть поле дата стрим и у мю. в итоге нужно будет вывести массив где можно будет посмотреть связь иедов и мю