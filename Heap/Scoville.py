# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 23:47:28 2021

@author: sokon
"""

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K and len(scoville)>1:
        min_val = heapq.heappop(scoville)
        second_val = heapq.heappop(scoville)
        heapq.heappush(scoville, min_val+second_val*2)
        answer+=1
    if scoville[0]<K:
        answer = -1
    return answer