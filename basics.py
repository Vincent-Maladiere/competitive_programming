class OurQueue:
    """Equivalent to deque.
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def append(self, el):
        self.in_stack.append(el)

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
    
    def pop(self):
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()
    

class OurHeap:
    """Equivalent to heapq.
    """
    def __init__(self, items):
        self.n = 0
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, el):
        if el in self.rank:
            raise ValueError("The item is already in the heap")
        self.heap.append(el)
        idx_el = len(self)
        self.rank[el] = idx_el
        self.up(idx_el)

    def pop(self):
        if len(self) <= 0:
            raise ValueError("No items to pop")

        min_val = self.heap.pop(1)
        max_val = self.heap.pop()
        self.heap.insert(1, max_val)
        del self.rank[min_val]
        self.down(1)
        return min_val
        
    def up(self, idx):
        parent_idx = idx // 2
        if parent_idx == 0:
            return
        el_parent = self.heap[parent_idx]
        el_child = self.heap[idx]
        if el_child < el_parent:
            # swap
            self.heap[parent_idx] = el_child
            self.heap[idx] = el_parent
            self.rank[el_child] = parent_idx
            self.rank[el_parent] = idx
            self.up(parent_idx)

    def down(self, idx):
        idx_lchild = idx * 2
        idx_rchild = idx_lchild + 1
        
        if idx_lchild > len(self):
            return
        
        el_parent = self.heap[idx]
        el_lchild = self.heap[idx_lchild]
        
        if idx_rchild > len(self) or el_lchild < self.heap[idx_rchild]:
            el_lowest_child = el_lchild
            idx_lowest_child = idx_lchild
        else:
            el_lowest_child = self.heap[idx_rchild]
            idx_lowest_child = idx_rchild
        
        if el_parent > el_lowest_child:
            # swap
            self.heap[idx_lowest_child] = el_parent
            self.heap[idx] = el_lowest_child
            self.rank[el_parent] = idx_lowest_child
            self.rank[el_lowest_child] = idx
            self.down(idx_lowest_child)

    def update(self, old, new):
        if new == old:
            return
        idx_old = self.rank.pop(old)
        self.rank[new] = idx_old
        self.heap[idx_old] = new
        if new < old:
            self.up(idx_old)
        else:
            self.down(idx_old)
