# %%
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    to_return = out = ListNode()

    while l1 or l2:

        if l1:
            out.val += l1.val
            l1 = l1.next
        
        if l2:
            out.val += l2.val
            l2 = l2.next


        index = out.val // 10
        out.val = out.val % 10

        if index or (l1 or l2):
            out.next = ListNode(val=index)
            out = out.next

    return to_return


def make_list_node(l_):

    head_l = l = ListNode()
    for idx, val in enumerate(l_):
        l.val = val
        if idx < len(l_) - 1:
            l.next = ListNode()
            l = l.next
    
    return head_l


l1 = make_list_node([1, 8])
l2 = make_list_node([0])
out = addTwoNumbers(l1, l2)
while out:
    print(out.val)
    out = out.next

# %%
