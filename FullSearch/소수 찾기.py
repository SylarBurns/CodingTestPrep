# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:51:57 2021

@author: sokon
"""
import itertools
def isprime(num):
    if num > 1:
        for i in range(2, num):
            if (num%i)==0:
                return False
        return True
    else:
        return False
def solution(numbers):
    answer = 0
    num_list = list(numbers)
    permuts=[]
    for i in range(1, len(numbers)+1):
        permuts+=itertools.permutations(num_list,i)
    permuts = [int(''.join(p)) for p in permuts]
    permuts = list(set(permuts))
    for p in permuts:
        if isprime(p):
            answer+=1
    return answer

numbers = "17"
print(solution(numbers))