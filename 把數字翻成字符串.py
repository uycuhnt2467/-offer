# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:07:53 2021

@author: a8520
"""


# 把數字翻譯成字符串

# 12258 -> return 5: 
# 1, 2, 2, 5, 8 [bccfi]
# 1, 22, 5, 8 [bwfi]
# 1, 2, 25, 8 [bczi]
# 12, 2, 5, 8 [mcfi]
# 12, 25, 8 [mzi]


class Solution:
    
    def get_translation_recursive(self, int_sequence):
        # recursive
        if int_sequence <= 0:
            return 0
        string = str(int_sequence)
        count = 0
        
        for len_ in range(1, len(string)+1):
            if int(string[:len_]) < 27:
                if len(string[len_:]) == 0:            
                    count += 1
                else:                
                    count += self.get_translation_recursive(int(string[len_:]))
        return count
    
    def get_translation_dp(self, int_sequence):
        # from right to left dynamically count:
        string = str(int_sequence)
        counts = [0] * len(string)
        
        for i in range(len(string)-1, -1, -1):
            count = 0
            if i == len(string) - 1:
                if 0 < int(string[i]) <= 9:
                    count += 1
            elif i == len(string) - 2:
                if 10 < int(string[i:]) < 27:
                    count += 1
                if 0< int(string[i]) < 27:
                    count += counts[i+1]
            else:
                if 10 <= int(string[i:i+2]) < 27:
                    count += counts[i+2]
                if 0 < int(string[i:i+1]) <= 9:
                    count += counts[i+1]
            counts[i] = count
        return counts[0]
    
    
sol = Solution()
test = 12258
print("result", sol.get_translation_recursive(test))
print("result", sol.get_translation_dp(test))
    
    
    
    
    
    
    
    
    
    
    
    
    
    