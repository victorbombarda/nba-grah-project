import numpy as np
import pandas as pd
from pyvis.network import Network
import sqlite3

salary18 = pd.read_csv(r"C:\Users\Lenovo01\Desktop\Grafo NBA - Bando de Dados\NBA_season1718_salary")
stats = pd.read_csv(r"C:\Users\Lenovo01\Desktop\Grafo NBA - Bando de Dados\Seasons_Stats_NBA")

stats_2017 = stats[stats["Year"] == 2017]

got_net = Network(notebook = True, height = "750px", width = "100%", bgcolor = "#222222", font_color = "white")

# set the physics layout of the network
got_net.barnes_hut()


sources = salary18['Player']
targets = salary18['Tm']
weights = salary18['season17_18']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title = src, shape = "box", value = 10000000)
    got_net.add_node(dst, dst, title = dst, shape = "star")
    got_net.add_edge(src, dst)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
#for node in got_net.nodes:
    #node["title"] += " Vizinhos:<br>" + "<br>".join(neighbor_map[node["id"]])
    #node["value"] = len(neighbor_map[node["id"]]) # this value attrribute for the node affects node size


got_net.showbuttons(filter = ['physics'])
got_net.showbuttons(filter = ["nodes"])
got_net.show("example.html")
