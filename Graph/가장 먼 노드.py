# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:52:13 2021

@author: sokon
"""

def solution(n, edge):
    graph = {}
    for i in range(1,n+1):
        graph[i]=[]
    for f, t in edge:
        graph[f].append(t)
        graph[t].append(f)
            
    def bfs(start, edges, n):
        distance = [-1]*n
        distance[start-1]=0
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            for child in graph[current_node]:
                if distance[child-1]==-1:
                    distance[child-1]= distance[current_node-1]+1
                    queue.append(child)
        
        max_dist = max(distance)
        return distance.count(max_dist)
    answer = bfs(1,edge,n)
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))