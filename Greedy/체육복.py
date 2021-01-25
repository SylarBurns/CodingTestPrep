# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:01:35 2021

@author: sokon
"""

def solution(n, lost, reserve):
    reserve_list = list(set(reserve)-set(lost))
    lost_list = list(set(lost)-set(reserve))
    lost_count = len(lost_list)
    for i, l in enumerate(lost_list):
        if l-1 in reserve_list:
            lost_count-=1
            reserve_list.pop(reserve_list.index(l-1))
        elif l+1 in reserve_list:
            lost_count-=1
            reserve_list.pop(reserve_list.index(l+1))
    return n-lost_count
    

n=3
lost =[3]
reserve = [1]
print(solution(n, lost, reserve))