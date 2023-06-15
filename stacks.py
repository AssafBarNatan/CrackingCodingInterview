#This document contains implementations of the exercises in 
#chapter 3 of cracking the coding interview

from collections import Counter
import numpy as np
import copy
import re

class minstack:
    """
    Implements a stack with an added function: min
    """
    def __init__(self, arr=[]):
        self.stack = []
        for el in arr:
            self.push(el)

    def push(self, el):
        if self.stack:
            _ , mval = self.stack[-1]
            if el < mval:
                self.stack.append((el, el))
            else:
                self.stack.append((el, mval))
        else:
            self.stack.append((el,el))

    def pop(self):
        if self.stack:
            el, _ = self.stack.pop()
            return el
        else:
            return None

    def min(self):
        if self.stack:
            _ , mval = self.stack[-1]
            return mval
        else:
            return None

class set_of_stacks:
    """
    Implements a stack of stacks
    """
    def __init__(self, arr=[], thresh = 10):
        self.thresh = 10
        self.stacklist = []
        self.stacklist.append([])
        for val in arr:
            self.push(val)

    def push(self, val):
        if len(self.stacklist[-1]) < thresh:
            self.stacklist[-1].append(val)
        else:
            self.stacklist.append([val])

    def pop(self):
        if self.stacklist[0] == []:
            return None
        if self.stacklist[-1] != []:
            return(self.stacklist[-1].pop())
        else:
            self.stacklist.pop()
            return self.pop()

    def change_thresh(self, thresh):
        return None

class queue:
    """
    Implements of a queue using two stacks
    """
    def __init__(self, arr=[]):
        self.instack = []
        self.outstack = []
        for val in arr:
            self.enqueue(val)

    def enqueue(self, val):
        self.instack.append(val)
        return None

    def dequeue(self):
        if self.outstack:
            return self.outstack.pop()
        else:
            while self.instack:
                self.outstack.append(self.instack.pop())
            if self.outstack:
                return self.outstack.pop()
            else:
                return None

    def peek(self):
        if self.outstack:
            return self.outstack[-1]
        else:
            while self.instack:
                self.outstack.append(self.instack.pop())
            if self.outstack:
                return self.outstack[-1]
            else:
                return None
                print("Queue is empty")

def sort_stack(stack):
    if len(stack) < 2:
        return stack

    holder = []
    #sorted_items = 0
    for i in range(len(stack)):
        val = stack.pop()
        while stack:
            compare = stack.pop()
            if compare > val:
                holder.append(compare)
            else:
                holder.append(val)
                val = compare
        holder.append(val)
        while holder:
            tmp = holder.pop()
            stack.append(tmp)
    return stack
