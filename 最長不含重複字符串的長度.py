# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 23:03:50 2021

@author: a8520
"""


# 48. 最長不含重複字符串的長度
# arabcacfr => return 4 因為 acfr為最長

class Solution:
    def longest_substring_without_duplication(self, strings):
        # brutal: 找所有子字串、判斷有無重複-> O(n**3)
        # 優化1: dp -> o(n**2)
        dp = [0] * len(strings)
        check_duplicate = [0] * len(strings)
        if not strings:
            return 0
        dp[0] = 1
        for i in range(1, len(strings)):
            count = 1
            prev = i - 1
            while prev >= 0 and check_duplicate[prev] == False:
                if strings[i] != strings[prev]:
                    count += 1
                else:
                    check_duplicate[prev] = True
                    break
                prev -= 1
            dp[i] = max(dp[i-1], count)
        return dp[-1]
    
    def longest_substring_without_duplication_2(self, strings):
        # 優化2:
        import string
        cur_len = 0
        max_len = 0
        
        pos_dict = dict()
        for i in string.ascii_lowercase:
            pos_dict[i] = -1
        
        for j in range(len(strings)):
            prev = pos_dict[strings[j]]
            if prev < 0 or j - prev > cur_len:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = j - prev
            pos_dict[strings[j]] = j
        
        if cur_len > max_len:
            max_len = cur_len
        return max_len
    

sol = Solution()
strings = "arabcacfr"
print(sol.longest_substring_without_duplication(strings))
print(sol.longest_substring_without_duplication_2(strings))