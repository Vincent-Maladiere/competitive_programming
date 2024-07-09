# %%
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def swap(ptr_a, ptr_b):
    c = ptr_a.val
    ptr_a.val = ptr_b.val
    ptr_b.val = c


def forward(ptr, steps):
    for _ in range(steps):
        ptr = ptr.next
    return ptr


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:

    # No-op
    if k == 1:
        return head
    
    is_k_even = (k % 2 == 0)
    
    n_nodes = 0
    ptr = head
    while ptr is not None:
        ptr = ptr.next
        n_nodes += 1

    n_group =  n_nodes // k
    ptr_start = head    

    for _ in range(n_group):

        ptr_half = ptr_start
        ptr_start_group = ptr_start
        #import ipdb; ipdb.set_trace()        

        # move to the middle
        half_k = k // 2
        ptr_half = forward(ptr_half, half_k)
        
        for steps in range(half_k - is_k_even, -1, -1):
            ptr_end = ptr_half
            ptr_end = forward(ptr_end, steps)
            swap(ptr_start_group, ptr_end)
            ptr_start_group = ptr_start_group.next
        
        ptr_start = forward(ptr_start, k)

    return head

            
def make_list_node(x):
    head = None
    for val in x:
        if head is None:
            node = ListNode(val)
            head = node
        else:
            node.next = ListNode(val)
            node = node.next
    return head


def print_list_node(head):
    while head is not None:
        print(head.val)
        head = head.next


x = [1, 2, 3, 4, 5, 6, 7]
k = 2
head = make_list_node(x)

head = reverseKGroup(head, k)
print_list_node(head)

# %%
