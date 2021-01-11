# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:45:48 2021

@author: a8520
"""


class Solution():
    def Power(self, base, exponent):
        
        if self.equal(base, 0.0) and exponent < 0:
            return 0.0
        # print("here", result)
        absExponent = exponent
        if exponent < 0:
            absExponent = -exponent
        
        result = self.PowerWithUnsignedExponent(base, absExponent)
        
        if exponent < 0:
            result = 1.0 / result
        return result
    def equal(self, val1, val2):
        if val1 - val2 < 0.000002 and val1 - val2 > - 0.000002:
            return True
        else:
            return False
    def PowerWithUnsignedExponent(self, base, absExponent):
        if absExponent == 0:
            return 1
        if absExponent == 1:
            return base
        result = self.PowerWithUnsignedExponent(base, absExponent >> 1)
        result *= result
        if absExponent & 0x1 == 1:
            result *= base
        return result
    
sol = Solution()
print(sol.Power(2.5, -3))