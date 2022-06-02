# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:55:35 2022

@author: Sayed
"""

graph = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
        }


def bfs(graph,startCity,endCity):
    
    visited=[]
    queue = [[startCity]]
    
    while queue:
        
        path = queue.pop(0)
        
        curCity = path[-1]
        
        if curCity not in visited:
            visited.append(curCity)
            
        visited.append(curCity)
        
        if curCity == endCity:
            print('path is: ',path)
            return path
        
        else:
            neighbourCities = graph.get(curCity,[])
            for city in neighbourCities:
                new_path = path.copy()
                new_path.append(city)
                queue.append(new_path)          
      
        

def dfs(graph,startCity,endCity):
    
    visited=[]
    queue = [[startCity]]
    
    while queue:
        
        path = queue.pop()
        
        curCity = path[-1]
        
        if curCity not in visited:
            visited.append(curCity)
            
        visited.append(curCity)
        
        if curCity == endCity:
            print('path is: ',path)
            return path
        else:
            neighbourCities = graph.get(curCity,[])
            for city in neighbourCities:
                new_path = path.copy()
                new_path.append(city)
                queue.append(new_path)          
      


bfs(graph,'Arad','Bucharest')
dfs(graph,'Arad','Bucharest')































