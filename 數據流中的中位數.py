# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:02:05 2021

@author: a8520
"""
# 41. 數據流中的中位數

# 如何得到數據流中的中位數? 如果數據量為奇數，則返回中間數字，否則返回中間兩個
# 數字的平均。

# 應用MaxHeap + MinHeap
import heapq

class Solution:
    def __init__(self):        
        self.max_heap = [] 
        self.min_heap = []
        self.len_max_heap = 0
        self.len_min_heap = 0
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
    
    def add(self, val):
        if self.len_max_heap == self.len_min_heap:
            if not self.max_heap:
                heapq.heappush(self.max_heap, -val)
                self.len_max_heap += 1
            else:
                # check larger then max in max_heap and smaller than min in min_heap
                if val >= -self.max_heap[0] and val < self.min_heap[0]:
                    heapq.heappush(self.max_heap, -val)
                elif val < -self.max_heap[0]:
                    heapq.heappush(self.max_heap, -val)
                else:
                    # val > self.min_heap[0]
                    temp = heapq.heappushpop(self.min_heap, val)
                    heapq.heappush(self.max_heap, -temp)
                self.len_max_heap += 1
        else:
            if not self.min_heap:
                heapq.heappush(self.min_heap, val)
                self.len_min_heap += 1
            else:
                
                # self.len_max_heap > self.len_min_heap
                if val >= -self.max_heap[0] and val < self.min_heap[0]:
                    heapq.heappush(self.min_heap, val)
                elif val > self.min_heap[0]:
                    heapq.heappush(self.min_heap, val)
                elif val == -self.max_heap[0]:
                    heapq.heappush(self.min_heap, val)
                else:
                    # val < -self.max_heap[0]
                    temp = heapq.heappushpop(self.max_heap, val)
                    heapq.heappush(self.min_heap, -temp)
                self.len_min_heap += 1
    def get_median(self):
        if self.len_max_heap == 0:
            return None
        
        if self.len_max_heap > self.len_min_heap:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
sol = Solution()
print(sol.get_median())
sol.add(1)
print(sol.get_median())
sol.add(1)
print(sol.get_median())
sol.add(2)
print(sol.get_median())
sol.add(3)
print(sol.get_median())


