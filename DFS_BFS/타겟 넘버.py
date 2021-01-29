# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:59:39 2021

@author: sokon
"""

def solution(numbers, target):
    answer = 0
    DP = [[0]]
    for i in range(len(numbers)):
        DP.append([0]*(2**(i+1)))
        for j in range(0, len(DP[i+1]), 2):
            DP[i+1][j]=DP[i][j//2]+numbers[i]
            DP[i+1][j+1]=DP[i][j//2]-numbers[i]
    
    answer = DP[len(numbers)].count(target)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))