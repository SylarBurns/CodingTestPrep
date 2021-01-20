# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:30:27 2021

@author: 
"""
import heapq
jobs = [[2, 6], [1, 9], [0, 3]]

def solution(jobs):
    answer = 0
    heap = []
    jobs_count = len(jobs)
    jobs=sorted(jobs)
    first_job = jobs.pop(0)
    finished_time = sum(first_job)
    finish_sum =first_job[1]
    while jobs:
        while jobs and jobs[0][0]<=finished_time:
            next_ele = jobs.pop(0)
            heapq.heappush(heap, (next_ele[1], next_ele[0]))
        if heap:
            next_job = heapq.heappop(heap)
            finished_time += next_job[0]
            finish_sum += finished_time-next_job[1]
        else:
            next_job = jobs.pop(0)
            finished_time = sum(next_job)
            finish_sum += finished_time-next_job[0]
    while heap:
        next_job = heapq.heappop(heap)
        finished_time += next_job[0]
        finish_sum += finished_time-next_job[1]
    answer = int(finish_sum/jobs_count)
    return answer

print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]))