# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:29:21 2021

@author: sokon
"""

def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and price<prices[stack[-1]]:
            j = stack.pop()
            answer[j]=i-j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices)-1-j
    
    return answer

prices = [1,2,3,2,3]
print(solution(prices))
