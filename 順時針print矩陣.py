# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:02:33 2021

@author: a8520
"""


# 
#  1  2  3  4 
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
#
# print: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10

class Solution:
    def print_matrix_clockwise(self, matrix, rows, cols):
        if not matrix or rows <= 0 or cols <= 0:
            return
        
        start = 0
        # step2. 確定終止條件
        while start < cols * 2 and start < rows * 2:
            # step1. 確定印的方式
            self.print_clockwise(matrix, cols, rows, start)
            start += 1
    
    def print_clockwise(self, matrix, cols, rows, start):
        end_x = cols - start - 1
        end_y = rows - start - 1
        
        # step3. 印的程式碼
        for i in range(start, end_x+1):
            print(matrix[start][i])
        
        # step4. 確定要繼續印的條件
        if start < end_y:
            # step3. 印的程式碼
            for j in range(start+1, end_y+1):
                print(matrix[j][end_x])
        
        # step4. 確定要繼續印的條件
        if start < end_x and start < end_y:
            # step3. 印的程式碼
            for i in range(end_x-1, start-1, -1):
                print(matrix[end_y][i])
        
        # step4. 確定要繼續印的條件
        if start < end_y-1 and start < end_x:
            # step3. 印的程式碼
            for j in range(end_y-1, start, -1):
                print(matrix[j][start])
                
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
rows = 4
cols = 4

sol = Solution()
sol.print_matrix_clockwise(matrix, rows, cols)

        
            
              