# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:50:51 2021

@author: sokon
"""


    
def solution(arrows):
    answer = 0
    op_list={0:[0,1],1:[1,1],2:[1,0],3:[1,-1],4:[0,-1],5:[-1,-1],6:[-1,0],7:[-1,1]}
    cord = {}
    path = {}
    q = []
    cur_cord = [0,0]
    q.append(cur_cord)
    cord[(cur_cord[0],cur_cord[1])]=0
    def next_cord(cur_cord, op):
        new_cord = cur_cord.copy()
        new_cord[0]+=op_list[op][0]
        new_cord[1]+=op_list[op][1]
        return new_cord
    
    for a in arrows:
        for i in range(2):
            new_cord = next_cord(cur_cord, a)
            cord[(new_cord[0], new_cord[1])] = 0
            path[(cur_cord[0], cur_cord[1], new_cord[0], new_cord[1])]=0
            path[(new_cord[0], new_cord[1], cur_cord[0], cur_cord[1])]=0
            q.append(new_cord)
            cur_cord = new_cord
    
    node = q.pop(0)
    cord[(node[0],node[1])]=1
    while q:
        new_node = q.pop(0)
        if cord[(new_node[0], new_node[1])] >=1:
            if path[(node[0], node[1], new_node[0], new_node[1])] == 0:
                answer+=1
                path[(node[0], node[1], new_node[0], new_node[1])] = 1
                path[(new_node[0], new_node[1], node[0], node[1])] = 1
        else:
            cord[(new_node[0], new_node[1])] = 1
            path[(node[0], node[1], new_node[0], new_node[1])] = 1
            path[(new_node[0], new_node[1], node[0], node[1])] = 1
        node = new_node
    return answer
arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))