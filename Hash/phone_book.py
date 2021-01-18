# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:01:30 2021

@author: sokon
"""
def solution(phone_book):
    answer = True
    phone_book.sort()
    prefix = []
    prefix.append(phone_book.pop(0))
    while len(phone_book) !=0:
        for p in prefix:
            for pnum in phone_book:
                if pnum.find(p) == 0:
                    return False
        prefix.append(phone_book.pop(0))
    return answer