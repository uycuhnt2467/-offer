# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:21:32 2021

@author: a8520
"""


class ListNode():
    def __init__(self, val = None, next_ = None):
        self.val = val
        self.next_ = next_

class Solution():
    def rough_find_previous_k(self, node, k):
        # traverse 2 time
        if not node or not k:
            return -1
        count = 0
        cur_node = node
        while cur_node.next_ != None:
            count += 1
            cur_node = cur_node.next_
        if count < k:
            return -1
        # find n - k + 1
        time = 0
        return_node = node
        while time < (count - k + 1):
            time += 1
            return_node = return_node.next_
        return return_node
    
    def find_previous_k(self, node, k):
        # traverse only 1 time 
        if not node or not k:
            return -1
        count = 0
        cur_node = node
        second_pointer = None
        while cur_node.next_ != None:
            count += 1
            if count == k:
                second_pointer = node
            cur_node = cur_node.next_
            if second_pointer != None:
                second_pointer = second_pointer.next_
        return second_pointer
    def find_previous_k_updated(self, node, k):
        # traverse only 1 time 
        # exception:
        # 1. node = None
        # 2. k > len(node)
        # 3. k = 0
        if not node or k==None:
            return -1
        count = 0
        cur_node = node
        second_pointer = None
        
        while cur_node.next_ != None:
            count += 1
            if count == k or k == 0:
                # print("here")
                k = 1
                second_pointer = node
            
            cur_node = cur_node.next_
            if second_pointer != None:
                second_pointer = second_pointer.next_
        
        return second_pointer

node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)
node5 = ListNode(5, node4)
node6 = ListNode(6, node5)
node7 = ListNode(7, node6)
node8 = ListNode(8, node7)

sol = Solution()
print(sol.rough_find_previous_k(node8, 3).val)
print(sol.find_previous_k(node8, 3).val)
print(sol.find_previous_k(node8,None))
print(sol.find_previous_k(None,2))
print(sol.find_previous_k(node8,0))
print(sol.find_previous_k_updated(node8,0).val)
print(sol.find_previous_k_updated(node8,9))


    
        