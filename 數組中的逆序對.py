# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 23:27:49 2021

@author: a8520
"""



# 51. 數組中的逆序對

class Solution:
    
    def inverse_pair(self, data):
        # merge sort and calculate
        # time complexity: nlog(n)
        # space complexity: n
        if not data:
            return 0
        
        copy = data[:]
        
        count = self.inverse_pair_core(data, copy, 0, len(data) - 1)
        return count
    
    def inverse_pair_core(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        
        length = int((end - start)/2)
        left = self.inverse_pair_core(copy, data, start, start + length)
        right = self.inverse_pair_core(copy, data, start + length + 1, end)
        
        i = start + length
        j = end 
        index_copy = end
        count = 0
        while i >= start and j >= (start + length + 1):
            if data[i] > data[j]:
                print("pair", data[i], data[j])
                copy[index_copy] = data[i]
                index_copy -= 1
                i -= 1
                count += (j - start - length)
                
            else:
                copy[index_copy] = data[j]
                index_copy -= 1
                j -= 1
            
        while i >= start:
            copy[index_copy] = data[i]
            index_copy -= 1
            # count += (j - start - length)
            i -= 1
            
        while j >= start + length + 1:
            copy[index_copy] = data[j]
            index_copy -= 1
            j -= 1
       
        print(left, right, count)
        return left + right + count
        

sol = Solution()
test = [7, 5, 6, 4]
print(sol.inverse_pair(test))