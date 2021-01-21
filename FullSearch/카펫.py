# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:34:37 2021

@author: sokon
"""

def solution(brown, yellow):
    answer = []
    for width in range(yellow, 0, -1):
        if yellow % width != 0:
            continue
        else:
            height = int(yellow / width)
        new_brown = (width+height)*2+4
        if new_brown == brown:
            answer = [width+2, height+2]
            break
    return answer
brown = 24
yellow = 24
print(solution(brown, yellow))