# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 08:44:33 2021

@author: a8520
"""


class Node:
    def __init__(self, val = None, next_ = None):
        self.val = val
        self.next_ = next_


# 如果linked list內包含環，如何找到環的入口節點。

class Solution:
    
    
    def findStart(self, node):
        # step1. 看快慢指針是否會重疊、會重疊代表有circle，進null代表沒
        ptr1 = node
        ptr2 = node
        
        step = 0
        while step < 2:
            if ptr1.next_ != None:
                ptr1 = ptr1.next_
            else:
                return -1
            step += 1
        if ptr2.next_ != None:
            ptr2 = ptr2.next_
        else:
            return -1
        
        circle = False
        count = 0
        # find circle
        while ptr1.next_ != None:
            if count == 0:
                ptr1 = ptr1.next_
                count = 1
            else:
                ptr1 = ptr1.next_
                ptr2 = ptr2.next_
                count = 0
            if ptr1 == ptr2:
                circle = True
                break
        if circle == False:
            return -1
        
        # step2. find the number of element in the circle，計算其中一個pointer花多久回到相遇的點
        count = 1
        ptr2 = ptr2.next_
        while ptr2 != ptr1:
            ptr2 = ptr2.next_
            count += 1
        
        # step3. 其中一個pointer先跑一個circle的步數後同時跑兩根指針，兩指針相遇的點就是環的起點
        ptr1 = node
        ptr2 = node
        step = 0
        while step < count:
            ptr1 = ptr1.next_
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next_
            ptr2 = ptr2.next_
        return ptr1
        
            
node = Node()