# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:38:05 2021

@author: sokon
"""

def solution(n, computers):
    answer = 0
    visited = [0]*n
    def dfs(init):
        stack=[init]
        while stack:
            com = stack.pop()
            if visited[com]==0:
                visited[com]=1
            for i in range(n):
                if computers[com][i]==1 and visited[i]==0:
                    stack.append(i)
    i = 0
    while sum(visited)!=n:
        if visited[i]==0:
            dfs(i)
            answer+=1
        i+=1
    return answer

n =3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))