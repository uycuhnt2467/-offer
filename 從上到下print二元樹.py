# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:15:47 2021

@author: a8520
"""

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def print_tree(self, node):
        if node == None:
            return
        dequeue = list()
        dequeue.append(node)
        while dequeue:
            cur_node = dequeue.pop(0)
            print(cur_node.val)
            if cur_node.left != None:
                dequeue.append(cur_node.left)
            if cur_node.right != None:
                dequeue.append(cur_node.right)
                
    def print_tree_layer(self, node):
        if node == None:
            return 
        dequeue = list()
        dequeue.append(node)
        start = 0
        end = start + 1
        while start < len(dequeue):
            print_string = ""
            next_end = end
            for node_num in range(start, end):
                print_string += str(dequeue[node_num].val) + " "
                if dequeue[node_num].left != None:
                    dequeue.append(dequeue[node_num].left)
                    next_end += 1
                if dequeue[node_num].right != None:
                    dequeue.append(dequeue[node_num].right)
                    next_end += 1
            print(print_string)
            start = end
            end = next_end
    def print_tree_layer_reverse(self, node):
        if node == None:
            return 
        
        dequeue = list()
        stack = list()
        dequeue.append(node)
        reverse = False
        while dequeue or stack:
            print_string = ""
            if not reverse:
                while dequeue:
                    cur_node = dequeue.pop(0)
                    print_string += str(cur_node.val) + " "                    
                    if cur_node.left != None:
                        stack.append(cur_node.left)                        
                    if cur_node.right != None:
                        stack.append(cur_node.right)                        
            else:
                while stack:
                    cur_node = stack.pop()
                    print_string += str(cur_node.val) + " "
                    if cur_node.right:
                        dequeue.insert(0, cur_node.right)
                    if cur_node.left:
                        dequeue.insert(0, cur_node.left)
            reverse = not reverse
            print(print_string)

            
o = TreeNode(15)
n = TreeNode(14)
m = TreeNode(13)
l = TreeNode(12)
k = TreeNode(11)
j = TreeNode(10)
i = TreeNode(9)
h = TreeNode(8)

g = TreeNode(7, n, o)
f = TreeNode(6, l, m)
e = TreeNode(5, j, k)
d = TreeNode(4, h, i)

c = TreeNode(3, f, g)
b = TreeNode(2, d, e)

a = TreeNode(1, b, c)
    
sol = Solution()
sol.print_tree(a)
sol.print_tree_layer(a)
sol.print_tree_layer_reverse(a)
        