#This document contains implementations of the exercises in 
#chapter 2 of cracking the coding interview

from collections import Counter
import numpy as np
import copy
import re

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> ' + repr(self.next)

    def __str__(self):
        return f'{self.val} -> ' + repr(self.next)
"""
class LinkedList:

    def __init__(self, unlinked_list=[], root=None):
        if unlinked_list and root:
            ret
"""

def linklist(L):
    """
    Takes a list and spits out a linked list
    """

    out = Node()
    writer = out
    for i in range(len(L)):
        writer.next = Node(L[i])
        writer = writer.next
    return out.next


def remove_dups(node):
    """
    Remove duplicates from an unsorted linked list.
    Follow-up: do this without a buffer
    """
    # Using a buffer
    mem = [node.val]
    ptr = node
    while ptr.next:
        if ptr.next.val in mem:
            ptr.next = ptr.next.next
        else:
            mem.append(ptr.next.val)
            ptr = ptr.next
    # not using a buffer
    follower = node
    while follower:
        scout = follower
        while scout.next:
            if scout.next.val == follower.val:
                scout.next = scout.next.next
            scout = scout.next
        follower = follower.next

def kth_last(node, k):
    """
    Return kth to last element in linked list
    """
    leader = node
    follower = node
    for i in range(k):
        if leader:
            leader = leader.next

    if leader is None:
        return None

    while leader:
        follower = follower.next
        leader = leader.next

    return follower.val

def delete_node(node, delnode):
    """
    delete delnode from the linked list, in place, 
    with only access to delnode
    """
    delnode.val = delnode.next.val
    delnode.next = delnode.next.next

def partition(node, val):
    """
    partitions a linked list around a value val such 
    that all nodes less than x come before all nodes 
    greater than x
    """
    start = Node(np.inf, node)
    pointer = start
    while pointer.next:
        if pointer.next.val <= val:
            start.val = pointer.next.val
            start = Node(0, start)
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next
    return start.next

def sum_lists(node1, node2):
    """
    Suppose linked lists represent two digit expansions of 
    numbers a and b. Return the digit expansion of a+b 
    as a linked list.

    1. Assume that the expansion is in reverse order
        ie: 1->2->3 is 321
    2. Assume that the expansion is NOT in reverse 
    order
    """
    # Assuming reverse order

    out = Node()
    writer = out
    carry = 0

    while node1 and node2 or carry:
        writer.next = Node()
        writer = writer.next
        val1 = (node1.val if node1 else 0)
        val2 = (node2.val if node2 else 0)
        carry, writer.val = divmod(val1 + val2 + carry, 10)
        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next
    if carry:
        writer
    return out.next
    
    # Assuming non-reverse order


def reverse_list(node):
    leader = copy.deepcopy(node)
    follower = None
    while leader:
        tmp = leader.next
        leader.next = follower
        follower = leader
        leader = tmp
    return follower


def palindrome(node):
    """
    checks if a linked list is a polindrome
    """
    revlist = reverse_list(node)
    while node:
        if not node.val == revlist.val:
            return False
        node = node.next
        revlist = revlist.next
    return True


def intersection(node1, node2):
    """
    Given two lists, determine if they intersect, 
    and return the intersecting node
    """
    # This piece of code finds the lengths 
    # of the two lists.
    runnerA = node1
    runnerB = node2
    lenA = 0
    lenB = 0
    while runnerA.next or runnerB.next:
        if runnerA.next is not None:
            lenA += 1
            runnerA = runnerA.next
        if runnerB.next is not None:
            lenB += 1
            runnerB = runnerB.next
    # If the end-nodes of the lists are not the 
    # same, then the lists are disjoint
    if not runnerA == runnerB:
        return None
    
    # This piece of code sets shortrun to 
    # the head of shorter list, and longrun 
    # to the head of the longer list
    if lenA < lenB:
        shortrun = node1
        longrun = node2
    else:
        shortrun = node2
        longrun = node1
    
    # equalize the tails of shortrun and longrun
    for i in range(max(lenA, lenB) - min(lenA, lenB)):
        longrun = longrun.next
    
    # find intersection
    while longrun and shortrun:
        if longrun == shortrun:
            return longrun
        longrun = longrun.next
        shortrun = shortrun.next
    
def detect_loop(node):
    """
    implement an algorithm that returns the node 
    at the beginning of a loop in the input 
    list. If no loop exists, return None
    """
    if node is None:
        return None
    if node.next is None:
        return None
    rabbit = node
    turtle = node
    intersect = False
    while rabbit and turtle:
        rabbit = rabbit.next
        turtle = turtle.next
        if rabbit is not None and not intersect:
            rabbit = rabbit.next
        if rabbit == turtle and not intersect:
            intersect = True
            rabbit = node
        if rabbit == turtle and intersect:
            return rabbit
    return None

mylist1 = linklist(np.random.randint(0,10,size=4))
mylist2 = linklist(np.random.randint(0,10,size=4))

print(mylist1)
print(mylist2)
print(sum_lists(mylist1, mylist2))

