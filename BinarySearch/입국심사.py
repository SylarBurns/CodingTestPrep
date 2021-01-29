# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:10:28 2021

@author: sokon
"""

def binary_search(left, right, times, n):
    count = 0
    answer = -1
    while left<=right:
        mid = int((left+right)/2)
        count = 0
        for t in times:
            count+=int(mid/t)
        
        if count >= n:
            if answer == -1:
                answer = mid
            else:
                answer = min(answer, mid)
            right = mid-1
        elif count < n:
            left= mid+1
    return answer

def solution(n, times):
    times.sort()
    left = 0
    right = times[-1]*n
    answer = binary_search(left, right, times, n)
    return answer

n = 6
times = [7, 10]
print(solution(n, times))