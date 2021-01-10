# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 21:06:33 2021

@author: a8520
"""


# dynamic programming and greedy
class Solution():
    def dp_maxProductAfterCutting(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [0] * (length + 1)
        products[1] = 1
        products[2] = 2
        products[3] = 3
        max_ = 0
        for i in range(4, length+1):
            # i = 4
            max_ = 0
            for j in range(1, (i//2)+1):
                # j = 1 and 2 =>
                # f(1) * f(3) and f(2) * f(2)
                product = products[j] * products[i - j]
                if max_ < product:
                    max_ = product
                
                products[i] = max_
        max_ = products[length]
        return max_
    def greedy_maxProductAfterCutting(self, length):
        # 每段線段越接近3則結果越大
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        timeOf3 = length // 3
        if length - timeOf3 * 3 == 1:
            timeOf3 -= 1
        timeOf2 = (length-timeOf3 *3) / 2
        
        return int(pow(3, timeOf3) * pow(2, timeOf2))
        
    
sol = Solution()
print(sol.dp_maxProductAfterCutting(10))
print(sol.greedy_maxProductAfterCutting(10))