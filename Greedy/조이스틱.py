# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:09:25 2021

@author: sokon
"""

def solution(name):
    ini_name = [ord("A")]*len(name)
    end_name = [ord(c) for c in name]
    offset = [0]*len(name)
    total_count = ord("Z")-ord("A")
    answer = 0
    cursor = 0
    for i in range(len(offset)):
        up_offset = end_name[i]-ini_name[i]
        down_offset = total_count-up_offset+1
        offset[i]=up_offset if up_offset<=down_offset else down_offset
    while True:
        if offset[cursor]!=0:
            answer+=offset[cursor]
            offset[cursor]=0
        right, move_right = right_offset(offset, cursor+1, cursor)
        left, left_move = left_offset(offset, cursor-1, cursor)
        if cursor == right and cursor == left:
            break
        else:
            answer += move_right if move_right<=left_move else left_move
            cursor = right if move_right<=left_move else left
        
    return answer
def right_offset(offsets, new_cursor, cursor):
    move = 1
    while True:
        if new_cursor>=len(offsets):
            new_cursor = 0
        if new_cursor == cursor:
            break
        if offsets[new_cursor]==0:
            move+=1
            new_cursor +=1
        elif offsets[new_cursor]!=0:
            break

    return new_cursor, move
def left_offset(offsets, new_cursor, cursor):
    move = 1
    while True:
        if new_cursor<0:
            new_cursor = len(offsets)-1
        if new_cursor == cursor:
            break
        if offsets[new_cursor]==0:
            move+=1
            new_cursor -=1
        elif offsets[new_cursor]!=0:
            break
    return new_cursor, move
name = "ABAAAAAAAAABB"
print(solution(name))