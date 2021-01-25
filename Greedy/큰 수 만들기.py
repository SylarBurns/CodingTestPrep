# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:11:10 2021

@author: sokon
"""

def solution(number, k):
    answer = ''
    answer_list = [number[0]]
    remove_count = 0
    for i in range(1,len(number)):
        target_num = number[i]
        if remove_count>=k:
            return ''.join(answer_list)+number[i:]
            break
        else:
            while answer_list and answer_list[-1]<number[i]:
                answer_list.pop()
                remove_count+=1
                if remove_count>=k:
                    break                    
            answer_list.append(target_num)
    answer= ''.join(answer_list)
    return answer[:len(number)-k]
number = '4177252841'
k = 4
print(solution(number, k))