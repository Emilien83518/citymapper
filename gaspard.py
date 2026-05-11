#Adjacency matrix 
import json 
with open("mini_reseau.json","r",encoding="utf-8") as f:
    data = json.load(f)  
def build_graph(data):
    graph={}
    for connection in data["connexions"]:
        A=connection["de"]
        B=connection["vers"]
        time=connection["temps"]
        if A not in graph:
            graph[A]=[] #creates an empty list for each station before appending it to the graph 
        graph[A].append((B,time)) 
    return graph
graph=build_graph(data)

def AdjM(graph):
    nodes = graph.keys()
    adjacency_matrix = [] 
    for node1 in nodes:
        row = []
        neighbours = graph[node1][0]
        for node2 in nodes:
            row.append(neighbours.count(node2))
        adjacency_matrix.append(row)
    return adjacency_matrix 
G={'Alpha': [('Bravo', 120)], 'Bravo': [('Alpha', 120), ('Charlie', 120)], 'Charlie': [('Bravo', 120), ('Delta', 120), ('Golf', 120), ('Hotel', 120)], 'Delta': [('Charlie', 120), ('Echo', 120)], 'Echo': [('Delta', 120)], 'Foxtrot': [('Golf', 120)], 'Golf': [('Foxtrot', 120), ('Charlie', 120)], 'Hotel': [('Charlie', 120), ('India', 120)], 'India': [('Hotel', 120), ('Juliet', 120)], 'Juliet': [('India', 120)]}
print(AdjM(G)) 
def bfs(G, s):
    color = dict()
    for x in G:
        color[x] = 'white'
    path = []
    color[s] = 'grey'
    history = [s]
    while history != []:
        current_vertex = history[0]
        path.append(current_vertex)
        for neighbor in G[current_vertex]:
            if color[neighbor] == 'white':
                color[neighbor] = 'grey'
                history.append(neighbor)
        history.pop(0)
        color[current_vertex] = 'black'
    return path