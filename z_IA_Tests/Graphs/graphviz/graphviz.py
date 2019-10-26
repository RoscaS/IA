from graphviz import Graph

graph = {'A': {'B', 'C'},
         'B': {'D', 'E'},
         'C': {'F'},
         'D': {},
         'E': {'F'},
         'F': {}}

g = Graph('G', filename='process.gv', engine='dot', )

for k, v in graph.items():
    for i in v:
        g.edge(k, i)

g.view()
