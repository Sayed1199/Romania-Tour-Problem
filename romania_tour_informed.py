# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:55:35 2022

@author: Sayed
"""

informed_graph={
    'Arad': [('Sibiu',140), ('Zerind',75), ('Timisoara',118)],
    'Zerind': [('Arad',75), ('Oradea',71)],
    'Oradea': [('Zerind',71), ('Sibiu',151)],
    'Sibiu': [('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu',80)],
    'Timisoara': [('Arad',118), ('Lugoj',111)],
    'Lugoj': [('Timisoara',111), ('Mehadia',70)],
    'Mehadia': [('Lugoj',70), ('Drobeta',75)],
    'Drobeta': [('Mehadia',75), ('Craiova',120)],
    'Craiova': [('Drobeta',120), ('Rimnicu',146), ('Pitesti',138)],
    'Rimnicu': [('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Fagaras': [('Sibiu',99), ('Bucharest',211)],
    'Pitesti': [('Rimnicu',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest': [('Fagaras',211), ('Pitesti',101), ('Giurgiu',90), ('Urziceni',85)],
    'Giurgiu': [('Bucharest',90)],
    'Urziceni': [('Bucharest',85),('Vaslui',142), ('Hirsova',98)],
    'Hirsova': [('Urziceni',98), ('Eforie',86)],
    'Eforie': [('Hirsova',86)],
    'Vaslui': [('Iasi',92), ('Urziceni',142)],
    'Iasi': [('Vaslui',92), ('Neamt',87)],
    'Neamt': [('Iasi',87)]
    }


h_table={
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie' : 161,
    'Fagaras' : 176,
    'Giurgiu' : 77,
    'Hirsowa' : 151,
    'Lasi' : 226,
    'Lugoj' : 244,
    'Mehadia' : 241,
    'Neamt' : 234,
    'Oradea' : 380,
    'Pitesti' : 100,
    'Rimnicu' : 193,
    'Sibiu' : 253,
    'Timisoara' : 329,
    'Urziceni' : 80,
    'Vaslui' : 199,
    'Zerind' : 374,
    }


def h_path_cost(path):
    
    last_node = path[-1][0]
    h_cost = h_table[last_node]
    return h_cost,last_node

    
def f_path_cost(path):
    g_cost=0
    for node,cost in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=h_table[last_node]
    f_cost = h_cost+g_cost
    return f_cost,last_node   





def greedyAlgorithm(graph,start_node,end_node,h_path_cost):
    
    visited=[]
    
    queue = [[(start_node,0)]]
    
    while queue:
        queue.sort(key=h_path_cost)
        path = queue.pop(0)
        curNode = path[-1][0]
        
        if curNode in visited:
            continue
        
        visited.append(curNode)
        
        if curNode == end_node:
            print('path: ',path )
            return path
        
        else:
            adjacentNodes = graph.get(curNode,[])
            for node,cost in adjacentNodes:
                new_path = path.copy()
                new_path.append((node,cost))
                queue.append(new_path)
                
                

def aStarAlgorithm(graph,start_node,end_node,f_path_cost):
    visited=[]
    queue=[[(start_node,0)]]
    while queue:
        queue.sort(key=f_path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        
        if node in visited:
            continue
        
        visited.append(node)
        if node == end_node:
            print('path: ',path)
            return path
        else:
            adjacent_nodes = graph.get(node,[])
            for node2,cost in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)                
                

greedyAlgorithm(informed_graph,'Arad', 'Bucharest', h_path_cost)  
aStarAlgorithm(informed_graph, 'Arad', 'Bucharest', f_path_cost)





























