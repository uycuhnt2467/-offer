# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:02:11 2021

@author: a8520
"""

import time 
# 60. n個骰子的點數
# 丟n個骰子，所有骰子朝上一面的點數和為s。輸入n，print出s所有可能的值出現的機率。

class Solution:
    def get_percentage_recursive(self, n):
        
        for total in range(n, 6 * n + 1):
            percentage = self.get_percentage_recursive_helper(n, total)
            print(f"Total: {total}, Percentage: {percentage}")
            
    def get_percentage_recursive_helper(self, n, total):
        cur_percentage = 0
        if n == 0:
            return 0
        
        for i in range(1, 7):
            if i > total:
                pass
            elif i == total and n > 1:
                pass
            elif i == total and n == 1:
                cur_percentage += 1
            else:
                cur_percentage += self.get_percentage_recursive_helper(n - 1, total - i)
            
        return cur_percentage
    
    
   
    
    def get_percentage_iterative(self, n):
        if n < 1:
            return 0
        
        probabilities_1 = [0] * ( 6 * n + 1)
        probabilities_2 = [0] * ( 6 * n + 1)
        probabilities = [probabilities_1, probabilities_2]
        flag = 0
        for i in range(1, 7):
            probabilities[flag][i] = 1
        
        for k in range(2, n + 1):
            for i in range(k):
                probabilities[1-flag][i] = 0
            
            for i in range(k, 6 * k + 1):
                probabilities[1-flag][i] = 0
                j = 1
                while j <= i and j <= 6:
                    probabilities[1-flag][i] += probabilities[flag][i-j]
                    j += 1
            flag = 1 - flag
        
        for i in range(n, 6 * n + 1):
            print(f"Total: {i}, Percentage: {probabilities[flag][i]}")
            
        
        
    
sol = Solution()

test = 6

start_time = time.time()
sol.get_percentage_recursive(test)
end_time = time.time()
print(f"----------Demend time = {end_time-start_time}----------")


start_time = time.time()
sol.get_percentage_iterative(test)
end_time = time.time()
print(f"----------Demend time = {end_time-start_time}----------")