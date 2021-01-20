# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:40:15 2021

@author: sokon
"""

def solution(operations):
    Q = []
    for operation in operations:
        op = operation[:1]
        num = int(operation[2:])
        if op == "I":
            Q.append(num)
            Q.sort()
        elif num == 1 and Q:
            Q.pop()
        elif Q:
            Q.pop(0)
    if Q:
        answer = [Q[-1], Q[0]]
    else:
        answer = [0,0]
    return answer
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))