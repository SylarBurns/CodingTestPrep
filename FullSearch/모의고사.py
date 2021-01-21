# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:29:50 2021

@author: sokon
"""

def solution(answers):
    answer = []
    correct_count = []
    for i in range(1,4):
        correct_count.append([0,i])
    routines = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ]
    for i, routine in enumerate(routines):
        for j, ans in enumerate(answers):
            if ans == routine[j%len(routine)]:
                correct_count[i][0]+=1
    correct_count.sort(reverse=True)
    max_count = correct_count[0][0]
    answer.append(correct_count[0][1])
    correct_count.pop(0)
    while correct_count:
        temp = correct_count.pop(0)
        if max_count == temp[0]:
            answer.append(temp[1])
        else:
            break
    answer.sort()
    return answer

answers = [1,3,2,4,2]
print(solution(answers))