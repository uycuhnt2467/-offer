# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:30:46 2021

@author: a8520
"""


# 實現兩個函式，分別用來序列化、反序列化二元樹

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left # smaller
        self.right = right # larger
        
        
class Solution:
    def serialize(self, node, current_string):
        if not node:
            return "$,"
        
        current_string += str(node.val) + ","
        current_string += self.serialize(node.left, "")
        current_string += self.serialize(node.right, "")
        return current_string
        
    
    def deserialize(self, serialize_string):
        if not serialize_string:
            return
        string_list = serialize_string.split(",")
        
        return self.deserialize_helper(None, string_list)
        
        
    def deserialize_helper(self, node, string_list):
        if not string_list:
            return
        
        if string_list[0] == "$":
            string_list.pop(0)
            return None
        
        node = Node()
        node.val = string_list.pop(0)
        node.left = self.deserialize_helper(None, string_list)
        node.right= self.deserialize_helper(None, string_list)
        return node


b = Node(6)
c = Node(5)
d = Node(4)

e = Node(3, c, b)
f = Node(2, d, None)
g = Node(1, f, e)

sol = Solution()
print(sol.serialize(g, ""))

test = "1,2,4,$,$,$,3,5,$,$,6,$,$"
ans = sol.deserialize(test)
print(sol.serialize(ans, ""))