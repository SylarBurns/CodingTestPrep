# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:54:02 2021

@author: sokon
"""

def solution(array, commands):
    answer = []
    for c in commands:
        temp = array[c[0]-1:c[1]]
        temp.sort()
        answer.append(temp[c[2]-1])
    return answer