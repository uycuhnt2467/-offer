# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 15:32:20 2021

@author: a8520
"""


class Solution():
    def __init__(self):
        self.path_length = 0
        
    def hasPath(self, matrix, rows, cols, string):
        if not matrix or not string or rows < 1 or cols < 1:
            return False
        
        visited = [False] * rows * cols
        
        self.path_length = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, string, visited):
                    return True
        return False
    
    def hasPathCore(self, matrix, rows, cols, row, col, string, visited):
        if self.path_length >= len(string):
            return True
        
        hasPath = False
        
        if row >= 0 and row < rows and col >= 0 and col < cols \
            and matrix[row * cols + col] == string[self.path_length] and visited[row * cols + col] == False:
                self.path_length += 1
                visited[row * cols + col] = True
                hasPath = self.hasPathCore(matrix, rows, cols, row + 1, col, string, visited) or\
                    self.hasPathCore(matrix, rows, cols, row - 1, col, string, visited) or\
                        self.hasPathCore(matrix, rows, cols, row, col + 1, string, visited) or\
                            self.hasPathCore(matrix, rows, cols, row, col - 1, string, visited)
                if hasPath == False:
                    self.path_length -= 1
                    visited[row * cols + col] = False
        return hasPath
                                
test = ["a", "b", "t", "g", "c", "f", "c", "s", "j", "d", "e", "h"]
rows = 3
cols = 4
find = "bfce"
sol = Solution()
print(sol.hasPath(test, rows, cols, find))

