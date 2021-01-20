# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:29:52 2021

@author: a8520
"""


class Solution:
    def number_of_1_between_1_and_N(self, num):
        if num <= 0:
            return 0
        str_num = str(num)
        return self.number_of_1(str_num)
    
    def number_of_1(self, str_num):
        if not str_num or str_num < "0" or str_num > "9":
            return 0
        
        first = str_num[0]
        len_str_num = len(str_num)
        
        if len_str_num == 1 and first == 0:
            return 0
        
        if len_str_num == 1 and first > 0:
            return 1
        
        num_first_digit = 0
        if first > 0:
            num_first_digit = self.power_base_10(len_str_num - 1)
        elif first == 1:
            num_first_digit = 2
        
        num_other_digits = first * (len_str_num - 1) * self.power_base_10(len_str_num - 2)
        num_recursive = self.number_of_1(str_num[1:])
        
        return num_first_digit + num_other_digits + num_recursive
    
    def power_base_10(self, num):
        result = 1
        for i in range(num):
            result *= 10
        return result
        