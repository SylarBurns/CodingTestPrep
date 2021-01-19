# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:42:18 2021

@author: sokon
"""

def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    total_weight = 0
    answer = 0
    while truck_weights:
        answer+=1
        total_weight -= bridge.pop(0)
        if (total_weight+truck_weights[0])<=weight:
            total_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    
    return answer+bridge_length