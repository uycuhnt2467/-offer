# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:23:36 2021

@author: a8520
"""


class Solution:
    def permutation(self, string):
        if not string:
            return 
        def split(word): 
            return [char for char in word] 
        string_list = split(string)
        self.permutation_helper(string_list, 0);
            
    def permutation_helper(self, string_list, i):
        if i == len(string_list):
            print("".join(string_list))
        else:
            start = i
            while start < len(string_list):
                temp = string_list[start]
                string_list[start] = string_list[i]
                string_list[i] = temp
                
                self.permutation_helper(string_list, i+1)
                
                temp = string_list[start]
                string_list[start] = string_list[i]
                string_list[i] = temp
                start += 1

sol = Solution()
test = "abcde"
sol.permutation(test)