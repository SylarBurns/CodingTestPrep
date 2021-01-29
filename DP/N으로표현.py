# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:59:56 2021

@author: sokon
"""

def solution(N, number):
    if N == number:
        return 1
    answer = -1
    DP = []
    for i in range(1,9):
        DP.append({int(str(N)*i)})
    for i in range(1,8):
        for j in range(i):
            for first in DP[j]:
                for second in DP[i-j-1]:
                    DP[i].add(first+second)
                    DP[i].add(first-second)
                    DP[i].add(first*second)
                    if second!=0:
                        DP[i].add(first//second)
        if number in DP[i]:
            answer = i+1
            break
    return answer

N = 5
number = 12
print(solution(N,number))