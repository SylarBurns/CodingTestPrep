# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:45:11 2021

@author: sokon
"""
def find_root(union, num):
    if union[num]!=num:
        union[num]=find_root(union, union[num])
    return union[num]
def merge(union, p1, p2):
    union[p2]=union[p1]

def solution(n, costs):
    bridges = 0
    answer = 0
    union = [i for i in range(n)]
    costs.sort(key=lambda x:x[2])
    for i in range(0,len(costs)):
        start, end, cost = costs[i]
        if find_root(union, start)==find_root(union, end):
            continue
        else:
            p1 = find_root(union, start)
            p2 = find_root(union, end)
            merge(union, p1, p2)
            answer+= cost
            bridges+=1
            if bridges == (n-1):
                break
    return answer

n = 4
costs =[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))