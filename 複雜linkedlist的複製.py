# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:20:24 2021

@author: a8520
"""


class Node:
    def __init__(self, val=None, sibling=None, next_=None):
        self.val = val
        self.next_ = next_
        self.sibling = sibling

class Solution:
    
    def copy_1(self, node):
        # traverse all node (N) to create new node based on next_
        # traverse n*n time to create sibling link
        # time: o(N*2)
        # space: 
        pass
    
    def copy_2(self, node):
        # store sibling pair in dictionary
        # traverse all node (N) to create new node and store pair in dicationary
        # traverse another all node to correct sibling pointer
        # time: o(N)
        # space: o(N)
        pass
    
    def copy_3(self, node):
        # time: o(N)
        # step 1. duplicate the node after itself
        if not node:
            return None
        
        cur = node
        while cur != None:
            new_node = Node(cur.val, cur.sibling, cur.next_)
            temp_next = cur.next_
            cur.next_ = new_node
            cur.next_.next_ = temp_next
            cur = cur.next_ # duplicate node
            cur = cur.next_ # next node
        # step 2. connect sibling (adjust sibling)
        cur = node
        count = 0
        while cur != None:
            if count % 2 == 0:
                pass
            else:
                if cur.sibling:
                    cur.sibling = cur.sibling.next_
            cur = cur.next_
            count += 1
        
        # step 3. separate list (adjust next)
        original = node
        new = node.next_
        
        cur_original = original
        cur_new = new
        
        cur = new.next_
        count = 0
        while cur != None:
            if count % 2 == 0:
                # add to original
                cur_original.next_ = cur
                cur_original = cur_original.next_
            else:
                # add to new
                cur_new.next_ = cur
                cur_new = cur_new.next_
            count += 1
            cur = cur.next_
        return new
c = Node(5)
a = Node(2,c,None)
b = Node(3,None,a)
c.next_ = b
c.sibling = a


sol = Solution()
ans = sol.copy_3(c)


            