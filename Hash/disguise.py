# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:22:27 2021

@author: sokon
"""
def solution(clothes):
    hash = {}
    answer = 1 
    for n, tp, in clothes:
        if tp in hash:
            hash[tp]+=1
        else:
            hash[tp]=2
    num_tps = list(hash.values())
    for tps in num_tps:
        answer*=tps
    return answer-1