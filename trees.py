#This document contains implementations of the exercises in 
#chapter 4 of cracking the coding interview

from collections import Counter
from collections import deque
import numpy as np

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '{} goes to {}'.format(self.val, repr(self.next))
    
    def __str__(self):
        return repr(self)

class LinkedList:
    """
    Implements a linked list
    """
    def __init__(self, nodelist=[]):
        self.head = ListNode()
        if nodelist:
            self.head = self.linklist(nodelist)


    def linklist(self, L):
        """
        Takes a list and spits out a linked list
        """
        out = ListNode()
        writer = out
        for i in range(len(L)):
            writer.next = ListNode(L[i])
            writer = writer.next
        return out.next

class GraphNode:
    """
    Implements a node in a graph
    """
    def __init__(self, nbrs=[], val=0):
        self.val = val
        self.nbrs = nbrs

class Graph:
    """
    Implements a graph class with some useful functions.
    To initialize, input a dict whose keys are the vertices and whose 
    values are the (directed) neigbours of that vertex
    """

    def __init__(self, adj_list = None):
        """
        adj_list is a dictionary object with {node : nbrs} where nbrs 
        is a list-type
        """
        self.dict = {}
        for node in adj_list.keys():
            self.add_node(node, adj_list[node])
            for nbr in adj_list[node]:
                self.add_node(nbr)

    def __repr__(self):
        return(str(self.dict))

    def get_nbrs(self, node):
        if node in self.get_nodes():
            return self.dict[node]
        else:
            print("Node not found")

    def get_nodes(self):
        return list(self.dict.keys())

    def add_node(self, node, nbrs = None):
        """
        adds the node to the graph, along 
        with its optional neighbours
        """
        if node in self.get_nodes():
            print("Node already exists")
        else:
            self.dict[node] = nbrs

    def add_edge(self, edge):
        """
        edge is a tuple
        """
        if edge[0] in self.get_nodes():
            self.dict[edge[0]].append(edge[1])
            if edge[1] not in self.get_nodes():
                self.add_node(edge[1])
            else:
                self.add_node(edge[0],[edge[1]])

    def ispath(self, S, E):
        """
        Finds out if there is a route from S (start) to E (end)
    
        If the graph is given as an adjacency matrix A and S and E 
        are indices, then bool(A^|A|) at (S,E) gives the answer. 
        This runs in O(n^3 log(n)) time, where n is the size of 
        the matrix. This also requires n^2 space
    
        I can do linear space and time using a breadth-first search
        """
        visited_nodes = set([])
        newnodes = queue.Queue()
        newnodes.add(S)
        while newnodes:
            check = newnodes.get()
            if check == E:
                return True
                for nbr in self.get_nbrs(check):
                    if nbr not in visited_nodes:
                        visited_nodes.add(nbr)
                        newnodes.add(nbr)
        return False

class bin_tree_node:
    """
    Implements a binary tree node
    """
    def __init__(self, left=None, right=None, val=0):
        self.val = val
        self.left = self.set_left(left)
        self.right = self.set_right(right)
        self.height = 0

    def get_height(self):
        if self.left is None and self.right is None:
            return 0
        return 1 + max(self.get_height(self.left),self.get_height(self.right))

    def __repr__(self):
        return str(self.val) + ' -> {' + repr(self.left) + ' , ' + repr(self.right) + '}'

    def __repr__(self):
        return str(self.val)

class BST:
    """
    Implements a binary search tree class
    """
    def __init__(self, nodelist=[], root=None):
        self.root = bin_tree_node()
        if root:
            self.root = root
        if nodelist:
            self.root = self.fromlist(nodelist)

    def __repr__(self):
        return repr(self.root)

    def fromlist(self, nodelist):
        """
        Given a sorted list, write an algorithm 
        to create a binary search tree with minimal height
        """
        unfilled = deque()
        root = bin_tree_node(val = nodelist[0])
        unfilled.append(root)

        for idx, val in enumerate(nodelist[1:]):
            writenode = unfilled.pop()
            if writenode.left == None:
                writenode.left = bin_tree_node(val = val)
                unfilled.append(writenode)
                unfilled.appendleft(writenode.left)
            elif writenode.right == None:
                writenode.right = bin_tree_node(val = val)
                unfilled.appendleft(writenode.right)
        return root

    def get_horizontals(self):
        """
        Returns a list of heads of linked lists corresponding 
        to the horizontal levels of the BST
        """
        out = [ListNode(self.root, None)]
        active_level = out[-1]
        while True:
            next_level_anchor = ListNode()
            next_level_writer = next_level_anchor
            while active_level:
                if active_level.val.left:
                    next_level_writer.next = ListNode(active_level.val.left)
                    next_level_writer = next_level_writer.next
                if active_level.val.right:
                    next_level_writer.next = ListNode(active_level.val.right)
                    next_level_writer = next_level_writer.next
                active_level = active_level.next
    
            if next_level_anchor.next is None:
                break
            out.append(next_level_anchor.next)
            active_level = next_level_anchor.next
        return out
"""
    def is_balanced(self):
        """
        Checks if the BST is balanced - balanced meaning that for every 
        node, the depth of left is at most one away from the depth of right
        """

        if self.root is None:
            return True
        if self.root.left is None or self.root.right is None:
            return True


        def height(node):
        
            if |height(self.root.left) - heigh(self.root.right)| < 2:
                return True
"""
mylist = range(50)
tree = BST(mylist)
print(tree)
horz = tree.get_horizontals()
for i in horz:
    print(i)
