# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:44:12 2021

@author: a8520
"""


class Solution():
    def checkString(self, string):
        # A[.[B]][e|EC] or .B[e|EC]
        # A: 整數、有正負號
        # C: 整數、有正負號
        # B: 無符號整數
        if not string:
            return False
        valid_string = set(["e", "E", "-", "+", ".", "0", "1", "2", \
                            "3", "4", "5", "6", "7", "8", "9"])
        string_ptr = 0
        
        point_appear_pos = []
        e_appear_pos = []
        sign_appear_pos = set()
        
        while string_ptr < len(string):
            if string[string_ptr] not in valid_string:
                return False
            if string[string_ptr] == "-" or string[string_ptr] == "+":
                if string_ptr - 1 in sign_appear_pos:
                    return False
                if e_appear_pos and point_appear_pos:
                    if e_appear_pos[0] > point_appear_pos[0]:
                        pass
                    else:
                        return False
                elif point_appear_pos:
                    return False
                sign_appear_pos.add(string_ptr)
            if string[string_ptr] == "e" or string[string_ptr] == "E":
                e_appear_pos.append(string_ptr)
                if string_ptr == len(string) - 1:
                    return False
            if string[string_ptr] == ".":
                if e_appear_pos:
                    return False
                if point_appear_pos:
                    return False
                point_appear_pos.append(string_ptr)
            string_ptr += 1
        return True
            

sol = Solution()
print(sol.checkString("+100")) #true
print(sol.checkString("5e2")) #true
print(sol.checkString("-123")) #true
print(sol.checkString("3.1416")) #true
print(sol.checkString("-1E-16")) #true
print(sol.checkString("12e")) #false
print(sol.checkString("1a3.14")) #false
print(sol.checkString("1.2.3")) #false
print(sol.checkString("+-5")) #false
print(sol.checkString("12e+5.4")) #false
print(sol.checkString("+5.-4")) #false
print(sol.checkString("+25.2e-4")) #false