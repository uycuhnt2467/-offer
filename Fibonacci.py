# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:09:18 2021

@author: a8520
"""


class Solution():
    def count_finbonacci(self, val):
        if val <= 0:
            return 0
        elif val == 1:
            return 1
        elif val >  1:
            return self.count_finbonacci(val - 1) + self.count_finbonacci(val - 2)
        else:
            pass
    
    def count_finbonacci2(self, val):
        current_list = [0, 1]
        if val <= 0:
            return 0
        if val == 1:
            return 1
        if val > 1:
            while val >= len(current_list):
                current_list.append(current_list[-1] + current_list[-2])
            return current_list[val]

sol = Solution()

print(sol.count_finbonacci(30))
print(sol.count_finbonacci2(30))