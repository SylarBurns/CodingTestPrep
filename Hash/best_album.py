# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:49:24 2021

@author: sokon
"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays =[500, 600, 150, 800, 2500]
def solution(genres, plays):
    answer = []
    play_per_g ={}
    for i in range(len(genres)):
        if genres[i] in play_per_g:
            play_per_g[genres[i]] += plays[i]
        else:
            play_per_g[genres[i]] = plays[i]
    play_per_g = sorted(play_per_g, key = lambda x : play_per_g[x], reverse=True)
    
    for g in play_per_g:
        temp = {}
        for i in range(len(genres)):
            if g == genres[i]:
                temp[i]=plays[i]
        temp = sorted(temp, key = lambda x : temp[x], reverse=True)[:2]
        for index in temp:
            answer.append(index)
    return answer

print(solution(genres, plays))