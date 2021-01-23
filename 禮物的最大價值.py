# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:17:54 2021

@author: a8520
"""


# 47. 禮物的最大價值
# 在一個m x n的棋盤的每一格都放一個禮物，每個禮物都有特定價值，你可以從左上角開始拿禮物
# 並且每次只能向右或向下移動一格，直到到達棋盤右下角，請問你最多能拿到多少價值的禮物?

# i.g. 
#  1v   10   3     8
# 12v    2   9     6
#  5v   7v   4    11
#  3    7v  16v   5v -> max = 53

class Solution:
    def get_max_value(self, matrix, rows, cols):      
        if not matrix:
            return 0     
        dp = [0] * len(matrix)
        for row_num in range(rows):
            for col_num in range(cols):
                if col_num != 0:
                    if row_num == 0:
                        dp[row_num * 4 + col_num] = \
                            dp[row_num * 4 + col_num - 1] + matrix[row_num * 4 + col_num]
                    else:
                        dp[row_num * 4 + col_num] = \
                            max(dp[row_num * 4 + col_num - 1], dp[(row_num-1) * 4 + col_num]) \
                                + matrix[row_num * 4 + col_num]
                else:
                    if row_num == 0:
                        dp[0] = matrix[0]
                    else:
                        dp[row_num * 4] = dp[(row_num-1) * 4] + matrix[row_num * 4]
        return dp[-1]

sol = Solution()
matrix = [1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5]
rows = 4
cols = 4
print(sol.get_max_value(matrix, rows, cols))