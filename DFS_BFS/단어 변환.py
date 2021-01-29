# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:48:00 2021

@author: sokon
"""

        

def solution(begin, target, words):
    if target not in words:
        return 0
    def get_matches(word, words):
        matching_words = []
        for w in words:
            unmatch_count = 0
            for i in range(len(word)):
                if w[i]!=word[i]:
                    unmatch_count+=1
            if unmatch_count == 1:
                matching_words.append(w)
        return matching_words
    
    graph = {}
    graph[begin] = get_matches(begin, words)
    for word in words:
        graph[word] = get_matches(word, words)
        
    def dfs(init):
        visit = [0 for i in words]
        stack = [init]
        count = 0
        while stack:
            node = stack.pop()
            if node == target:
                return count
            for i in range(0,len(words)):
                if words[i] in graph[node]:
                    if visit[i]!=0:
                        continue
                    visit[i]=1
                    stack.append(words[i])
            count+=1
            
    answer = dfs(begin)
    return answer

words = ["hot", "dot", "dog", "lot", "log", "cog"]
target = "cog"
begin = "hit"

print(solution(begin, target, words))