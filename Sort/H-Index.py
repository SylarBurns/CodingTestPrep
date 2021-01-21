# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 00:08:48 2021

@author: sokon
"""

def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for c in citations:
        answer+=1
        if c < answer:
            answer-=1
            break
    return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))