# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:03:40 2021

@author: sokon
"""
def solution(people, limit):
    answer = 0
    start = 0
    end = len(people)-1
    people.sort(reverse= True)
    while start<=end:
        boat = people[start]
        start+=1
        if boat != limit:
            while start<=end:
                if boat+people[end]<=limit:
                    boat+=people[end]
                    end+=1
                else:
                    break
        answer+=1
    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))