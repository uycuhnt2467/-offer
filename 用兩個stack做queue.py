# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:11:37 2021

@author: a8520
"""



class Solution():
    
    def __init__(self):
        self.stackS = []
        self.stackR = []
    
    def appendTail(self, val):
        while self.stackR:
            self.stackS.append(self.stackR.pop())
        self.stackS.append(val)
    
    def deleteHead(self):
        while self.stackS:
            self.stackR.append(self.stackS.pop())
        if len(self.stackR) > 0:
            self.stackR.pop()
        
        while self.stackR:
            self.stackS.append(self.stackR.pop())
    
class Solution2():
    
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def append(self, val):
        while self.queue2:
            self.queue1.append(self.queue2.pop())
        self.queue1.append(val)
    
    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1.pop()
        while self.queue2:
            self.queue1.append(self.queue2.pop())
        
        