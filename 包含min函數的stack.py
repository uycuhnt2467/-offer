# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:29:52 2021

@author: a8520
"""


# 定義一個stack的數據結構，可以得到stack的最小元素
# 調用 min, pop push時間複雜度均為O(1)


class Solution:
    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        
    def push(self, num):
        self.stack.append(num)
        
        if len(self.min_stack) > 0:
            if self.min_stack[len(self.min_stack)-1] >= num:
                self.min_stack.append(num)
            else:
                self.min_stack.append(self.min_stack[len(self.min_stack)-1])
        else:
            self.min_stack.append(num)
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def min_(self):
        if self.min_stack:
            return self.min_stack[len(self.min_stack) - 1]
        else:
            return None

sol = Solution()
print(sol.min_())

sol.push(3)
sol.push(1)
sol.push(5)
print(sol.min_())
sol.pop()
print(sol.min_())
sol.pop()
print(sol.min_())
        
                
        