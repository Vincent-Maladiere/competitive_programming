# %%

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return None

    right = root.right
    root.right = flatten(root.left)
    root.left = None

    head = root
    while head.right is not None:
        head = head.right
    head.right = flatten(right)

    return root


def preorder(root):
    if root is not None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.right = TreeNode(6)
root.right.right = TreeNode(7)


root = flatten(root)
preorder(root)

# %%
