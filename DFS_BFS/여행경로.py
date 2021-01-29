# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:54:06 2021

@author: sokon
"""

def solution(tickets):
    graph = {}
    for f, t in tickets:
        if f not in graph:
            graph[f] = [t]
        else:
            temp = list(graph[f].copy())
            temp.append(t)
            graph[f] = temp
    for f, t in tickets:
        temp = list(graph[f].copy())
        temp.sort()
        graph[f] = temp
        
    def dfs(init):
        stack = [init]
        route = []
        while stack:
            node = stack[-1]
            if node not in graph or len(graph[node])==0:
                route.append(stack.pop())
            else:
                stack.append(graph[node].pop(0))
        return route
    answer = dfs("ICN")
    answer.reverse()
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))