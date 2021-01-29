# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:22:03 2021

@author: sokon
"""

def solution(money):
    DP = [0]*len(money)
    DP[0] = money[0]
    for i in range(1, len(DP)-1):
        DP[i]= max(DP[i-1], money[i]+DP[i-2])
    attempt1 = max(DP)
    DP = [0]*len(money)
    DP[1] = money[1]
    for i in range(2, len(DP)):
        DP[i]= max(DP[i-1], money[i]+DP[i-2])
    attempt2 = max(DP)
    return max(attempt1, attempt2)