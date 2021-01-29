# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:56:33 2021

@author: sokon
"""

def solution(n, results):
    answer = 0
    lose_win = {}
    win_lose ={}
    for i in range(1,n+1):
        lose_win[i]=[]
        win_lose[i]=[]
    for w, l in results:
        lose_win[l].append(w)
        win_lose[w].append(l)
        
    for i in range(1,n+1):
        win_set =set([])#i가 이긴 선수들
        lose_set =set([])#i가 진 선수들
        
        win_visit = []
        stack = [i]
        while stack:
            node = stack.pop(0)
            if node not in win_visit:
                win_visit.append(node)
                stack.extend(win_lose[node])
                win_set.update(win_lose[node])
        lose_visit = []
        stack = [i]
        while stack:
            node = stack.pop(0)
            if node not in lose_visit:
                lose_visit.append(node)
                stack.extend(lose_win[node])
                lose_set.update(lose_win[node])
        if (len(win_set.union(lose_set)) == n-1):
            answer += 1
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))