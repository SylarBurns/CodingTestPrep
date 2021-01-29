# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:20:30 2021

@author: sokon
"""

def solution(triangle):
    answer=0
    for i in range(len(triangle)-1,0,-1):
        for j in range(len(triangle[i])-1):
            triangle[i-1][j]+=max(triangle[i][j],triangle[i][j+1])
    answer = triangle[0][0]
    return answer


    
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
    