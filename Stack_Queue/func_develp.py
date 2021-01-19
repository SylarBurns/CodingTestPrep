# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:21:36 2021

@author: sokon
"""
import math
def solution(progresses, speeds):
    answer = []
    stack = [0]*len(progresses)
    for i in range(len(stack)):
        stack[i] = math.ceil((100-progresses[i])/speeds[i])
    while stack:
        temp = stack.pop(0)
        c = 1
        while stack and temp >= stack[0]:
            c+=1
            stack.pop(0)
        answer.append(c)
    return answer

progresses = [93,30,55]
speeds = [1, 30,5]
print(solution(progresses, speeds))