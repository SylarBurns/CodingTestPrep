# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:49:18 2021

@author: sokon
"""

def solution(routes):
    routes.sort()
    cameras=[]
    dealt_with=[]
    for route in routes:
        if not cameras:
            cameras.append(route.copy())
            dealt_with.append(route.copy())
        else:
            for cam in cameras:
                if cam[0]>route[1] or cam[1]<route[0]:
                    continue
                elif cam[0]<=route[0] or cam[1]>=route[1]:
                    cam[0] = max(cam[0], route[0])
                    cam[1] = min(cam[1], route[1])
                    dealt_with.append(route)
                    break
            if route not in dealt_with:
                cameras.append(route)
                dealt_with.append(route)
    return len(cameras)

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))