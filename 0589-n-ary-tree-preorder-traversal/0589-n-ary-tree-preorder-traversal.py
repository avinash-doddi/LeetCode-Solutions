"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def pre(root):
            if (root == None): return
            arr.append(root.val);
            for i in root.children:
                pre(i);
        pre(root)
        return arr;