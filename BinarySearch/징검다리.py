# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:58:32 2021

@author: sokon
"""
def binary_search(left, right, rocks, n):
    answer = 0
    while left<=right:
        mid = (left+right)//2
        prev = 0
        min_val = 10000000001
        count = 0
        for r in rocks:
            if r-prev<mid:
                count+=1
                if count>n: break
            else:
                min_val = min(min_val, mid)
                prev = r
        if count>n:
            right = mid-1
        else:
            answer = min_val
            left = mid+1
    return answer
def solution(distance, rocks, n):
    if len(rocks)==n:
        return distance
    rocks.sort()
    left = 1
    right = distance
    answer = binary_search(left, right, rocks, n)
    return answer
distance = 25
rocks = [2,14,11,21,17]
n = 2
print(solution(distance, rocks, n))