# coding utf-8
#------Auto Drawing Production Line Flow Diagram------
from graphviz import Digraph
import pandas as pd

#Loading production line description file (json)
orgdata=pd.read_json('production_line_description.json')

#Data Processing
stationlist=pd.DataFrame(orgdata['production_line']['station'])
vstationlist=pd.DataFrame(orgdata['production_line']['virtual_station'])
flowlist=pd.DataFrame(orgdata['production_line']['flow'])


#---Draw Diagram---
dot = Digraph(comment='Production Line Diagram', format='png')
dot.node('START', 'Start')
dot.node('END', 'End')

#Establish Station Node
for i in range(len(stationlist.T)):
    dot.node(stationlist.loc['Name'][i], stationlist.loc['Text'][i],shape='rectangle')

#Establish Virtual_Station Node
for i in range(len(vstationlist.T)):
    dot.node(vstationlist.loc['Name'][i], vstationlist.loc['Text'][i],shape='rectangle')

#Establish Flow Line
for i in range(len(flowlist.T)):
    dot.edge(flowlist.loc['Origin'][i], flowlist.loc['Destination'][i], flowlist.loc['Text'][i])

dot.view()
print(str(len(stationlist.T)))
#---