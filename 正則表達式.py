# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:44:25 2021

@author: a8520
"""

# 正則表達式
# .(any one character) 和 *(0-many)
class Solution():
    def re(self, pattern, string):
        if len(pattern) == 0:
            return False
        if pattern[0] == "*":
            return False
        if len(string) == 0:
            return False
        
        star_pos = set()
        for i in range(len(pattern)):
            
            if pattern[i] == "*":
                star_pos.add(i)
                if i > 0 and pattern[i] == pattern[i-1]:
                    return False
                
        string_ptr = 0
        pattern_ptr = 0
        
        cur_char = string[0]
        while string_ptr < len(string) and pattern_ptr < len(pattern):
            # print("sp", string_ptr)
            # print("pp", pattern_ptr)
            if pattern[pattern_ptr] != "*":
                if string[string_ptr] == pattern[pattern_ptr] \
                    or pattern[pattern_ptr] == ".":
                    string_ptr += 1
                    pattern_ptr += 1
                    if pattern_ptr < len(pattern) \
                        and pattern[pattern_ptr] == "*":
                        cur_char = pattern[pattern_ptr - 1]   
                else:
                    # check whether next is * (could be 0 - many)
                    # aa_
                    # ab*_
                    if (pattern_ptr + 1) in star_pos:
                        pattern_ptr += 2
                    else:
                        return False
            else:
                if string[string_ptr] == cur_char:
                    string_ptr += 1
                else:
                    pattern_ptr += 1
       
        if string_ptr == len(string) and pattern_ptr == len(pattern):
           return True
        return False
        
        
sol = Solution()
print(sol.re("a.a", "aaa"))
print(sol.re("ab*ab*a", "aaa"))
print(sol.re(".", "aaa"))
print(sol.re("...", "aaa"))
print(sol.re(".a.", "aaa"))
print(sol.re(".b.", "aaa"))
print(sol.re("b.", "aaa"))
print(sol.re("b..", "aaa"))
print(sol.re("b..", ""))
print(sol.re("", "aaa"))
print(sol.re("....", "aaa"))