"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_2_new = {None: None}
        
        old = head

        while old:
            old_2_new[old] = Node(old.val)
            old = old.next

        old = head
        while old:
            new = old_2_new[new]
            new.next = old_2_new[new.next]
            new.random = old_2_new[new.random]
            old = old.next
            
        return old_2_new[head]
