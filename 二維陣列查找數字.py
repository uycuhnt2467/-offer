# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:05:11 2021

@author: a8520
"""



test = [[1,2,8,9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]


def findTarget(array, target):
    
    row = 0
    col = len(array[0]) - 1
    
    while row < len(array[0]) and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] > target:
            col -= 1
        else:
            row += 1
        
    return False
    
# 變體: double binary search
    
        