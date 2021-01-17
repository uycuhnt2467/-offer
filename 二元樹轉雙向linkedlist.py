# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:04:06 2021

@author: a8520
"""


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left # smaller
        self.right = right # larger


class Solution:
    
    def convert(self, node):
        pass
    
    def convert_node(self, node):
        pass
    
    
    
    def traverse(self, node):
        if not node:
            return None
        if node.left:
            node.left = self.traverse(node.left)
            precessor = self.find_preccessor(node)
            precessor.right = node
            node.left = precessor
        
        if node.right:
            node.right = self.traverse(node.right)
            successor = self.find_successor(node)
            node.right = successor
            successor.left = node
        
        return node
    
    def find_preccessor(self, node):
        cur = node.left
        while cur.right != None:
            if cur.val < cur.right.val:
                cur = cur.right
            else:
                break
        return cur
    
    def find_successor(self, node):
        cur = node.right
        while cur.left != None:
            if cur.val > cur.left.val:
                cur = cur.left
            else:
                break
        return cur
    
    def print_left(self, node):
        if not node:
            return
        cur = node
        print(cur.val)
        while cur.left and cur.left.val < cur.val:
            print(cur.left.val)
            cur = cur.left
    
    def print_right(self, node):
        if not node:
            return
        cur = node
        print(cur.val)
        while cur.right and cur.right.val > cur.val:
            print(cur.right.val)
            cur = cur.right
    
    def check_ans(self, node):
        while node.left != None:
            node = node.left
        
        while node.right != None:
            if node.right.left != node:
                return False
            node = node.right
        while node.left != None:
            if node.left.right != node:
                return False
            node = node.left
        return True
a = Node(5)
b = Node(15)
c = Node(10, a, b)
sol = Solution()
ans = sol.traverse(c)



a = Node(16)
b = Node(12)
c = Node(8)
d = Node(4)

e = Node(14, b, a)
f = Node(6, d, c)
g = Node(10, f, e)

sol = Solution()
ans = sol.traverse(g)
sol.print_right(ans)
sol.print_left(ans)
print(sol.check_ans(ans))