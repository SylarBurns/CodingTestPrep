# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:20:05 2021

@author: sokon
"""

def solution(participant, completion):
    hash = {}
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    for p in completion:
        if hash[p]>1:
            hash[p] -= 1
        else:
            del hash[p]
    answer = list(hash.keys())[0]
    return answer