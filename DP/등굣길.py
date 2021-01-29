# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:22:48 2021

@author: sokon
"""

def solution(m, n, puddles):
    dp = [[1]*m for i in range(n)]
    for puddle in puddles:
        x=puddle[1]-1
        y=puddle[0]-1
        dp[y][x]=0
        if x == 0:
            for i in range(y,n):
                dp[0][i] = 0
        if y == 0:
            for i in range(x,m):
                dp[i][0] = 0
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j]!=0:
                dp[i][j]= dp[i-1][j]+dp[i][j-1]
    answer = dp[n-1][m-1]
    return answer%1000000007

m = 4
n= 3
puddles = [[2,2]]
print(solution(m,n,puddles))