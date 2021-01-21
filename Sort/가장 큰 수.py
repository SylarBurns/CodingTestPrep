# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:59:53 2021

@author: sokon
"""

def solution(numbers):
    answer = ''
    num_list = [str(num) for num in numbers] 
    num_pair_list = []
    for num in num_list:
        origin_num = num
        i = 0
        while len(num)<4:
            num += origin_num[i]
            i = (i+1)%len(origin_num)
        num_pair_list.append([num, origin_num])
    num_pair_list.sort(reverse = True)
    for num in num_pair_list:
        answer+=num[1]
    return str(int(answer))