# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:26:01 2021

@author: sokon
"""
priorities = [1,1,9,1,1,1]
location = 0
def solution(priorities, location):
    printed_index = []
    unprinted_index = [i for i in range(len(priorities))]
    while True:
        if len(priorities)==1:
            printed_index.append(unprinted_index.pop(0))
            break
        if priorities[0]>=max(priorities[1:]):
            printed_index.append(unprinted_index.pop(0))
            priorities.pop(0)
            if printed_index[-1]==location:
                break
        else:
            priorities.append(priorities.pop(0))
            unprinted_index.append(unprinted_index.pop(0))

    answer = printed_index.index(location)+1
    return answer

print(solution(priorities,location))