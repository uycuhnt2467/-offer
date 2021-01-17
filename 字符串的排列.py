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
                
    def choose(self, string):
        if not string:
            return
        def split(word):
            return [char for char in word]
        string_list = split(string)
        
        for i in range(len(string_list)): # 第i個字符開始處理
            for j in range(len(string_list) - i + 1): # 目前字串總長度
                self.choose_help(string_list, i, j, []) 
    
    def choose_help(self, string_list, i, len_, temp_string):
        temp_string.append(string_list[i])
        if len_ == 0:
            print("".join(temp_string))
        else:
            next_ = i + 1
            for k in range(next_, len(string_list)):
                self.choose_help(string_list, k, len_-1, temp_string)
        temp_string.pop()
    
        
    
   
        
        
        
        
sol = Solution()
test = "abcde"
# sol.permutation(test)

sol.choose("abcd")