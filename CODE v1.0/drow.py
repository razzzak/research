import random
from osob import Osob
from ied import IED 
from switch import Switch
from port import Port
from physical_link import Physical_link
import networkx as nx
import math
from logical_conn import Logical_conn
import matplotlib as mpl
import matplotlib.pyplot as plt
#визуализация

class Drow:
    def draw_graph(self):
        pass
    def __init__(self, osob, logical_conns,MU, Terminal, Switch):
        self.MU=MU
        self.Terminal=Terminal
        self.Switch = Switch
        self.Log_Con=logical_conns
        self.osob=osob
        G=nx.Graph() #граф физ связей
        F=nx.Graph() #граф лог связей
        colors = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'purple', 'red','yellow','brown']
        #for edge in osob.ph_link+self.Log_Con:
        graph_pos={}
        weights_ph=[]
        colorss_ph=[]
        MUs=[]
        Terms=[]
        Switches=[]
        for phl in self.osob.ph_link:
            G.add_edge(phl.home.name, phl.end.name, weight=(phl.weight*1.0))
            graph_pos[phl.home.name]=[phl.home.coords.x,phl.home.coords.y]
            graph_pos[phl.end.name]=[phl.end.coords.x,phl.end.coords.y]
            colorss_ph.append(random.choice(colors))
            weights_ph.append(phl.weight*1.0*2.0)
            phl.weight=1
        for mu1 in self.MU:
            MUs.append(mu1.name)
        for term1 in self.Terminal:
            Terms.append(term1.name)
        for sw in self.Switch:
            Switches.append(sw.name)

        #dobavim Astar
        
        flows=[]
        edges=[]
        colorss=[]
        weights=[]
        grap=[]
        r=5

        #nx.draw_networkx_edges(G, graph_pos, width=weights_ph, edge_color='black')
       
        for log in self.Log_Con:
            log_h=log.home.name
            log_e=log.end.name
            f = nx.astar_path(G,log_h,log_e)
            flows.append(f)
            G.add_path([f])     
        dtx=1
        dty=5
        for f_num,f in enumerate(flows):
            Fl=nx.Graph()
            edges=[]
            colorss=[]
            colorss.append(random.choice(colors))
            for n in range (len(f)-2):
                colorss.append(colorss[-1])
            for n in range (len(f)-1):
                route_edges=(f[n],f[n+1])  
                edges.append(route_edges)
            print(f)
            print(edges)
            Fl.add_edges_from(edges)
            Fl.add_nodes_from(f)
            print("Graph has %d nodes with %d edges" %(Fl.number_of_nodes(),Fl.number_of_edges()))
            #dtx=r*math.sin(f_num*(2*math.pi/len(flows))) 
            #dty=r*math.cos(f_num*(2*math.pi/len(flows)))
            dtx+=1
            dty+=5
            print(dty)
            graphp_pos={}
            print(edges)
            for item in self.osob.ph_link:
                if isinstance(item.home,Switch) and isinstance(item.end,Switch):
                    graphp_pos[item.home.name]=[item.home.coords.x,item.home.coords.y+dty]
                    graphp_pos[item.end.name]=[item.end.coords.x,item.end.coords.y+dty]
                else:
                    graphp_pos[item.home.name]=[item.home.coords.x+dtx,item.home.coords.y]
                    graphp_pos[item.end.name]=[item.end.coords.x+dtx,item.end.coords.y]
            nx.draw_networkx_edges(Fl, graphp_pos, edgelist=edges, width=3, edge_color=colorss)
            
        #for f in colorss:
         #   print (f)
            
        for edge in self.Log_Con:
            F.add_edge(edge.home.name, edge.end.name)
        #создадим координаты для логических связей
        graphlog_pos={}
        for item in self.Log_Con:
            graphlog_pos[item.home.name]=[item.home.coords.x+2,item.home.coords.y+2]
            graphlog_pos[item.end.name]=[item.end.coords.x+2,item.end.coords.y+2]
        #print (graphlog_pos)
        #nx.draw_networkx_edges(G, graph_pos, width=weights_ph, edge_color='yellow')
        # нарисуем потоки в соотв с Астар
        
        
            #nx.draw_networkx_edges(Fl, grap[ctr], edgelist=edgelist, width=3, edge_color=colorss[ctr])
        # нарисуем физ.связи
        #nx.draw_networkx_edges(G, graph_pos, edgelist=graph, edge_size=5, edge_color='black') 
        #nx.draw_networkx_edges(G, graph_pos, edgelist=graphlog, edge_size=5, edge_color='yellow')
        #nx.draw_networkx_nodes(G, graph_pos,  node_size=500, node_color='red', alpha=1.0)
        nx.draw_networkx_edges(F, graphlog_pos, edge_size=10, edge_color='black', style='dashed')
        nx.draw_networkx_nodes(G, graph_pos, nodelist=MUs, node_size=1000, node_color='red', node_shape='h', alpha=1.0)
        nx.draw_networkx_nodes(G, graph_pos, nodelist=Terms, node_size=1000, node_color='blue', node_shape='o', alpha=1.0) 
        nx.draw_networkx_nodes(G, graph_pos, nodelist=Switches, node_size=2000, node_color='green', node_shape='s', alpha=1.0) 
        nx.draw_networkx_labels(G, graph_pos, font_size=8, font_family='sans-serif')
        plt.show()
