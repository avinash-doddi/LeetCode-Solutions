"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None: return []
        from collections import deque as dq, defaultdict as maps
        queue = dq([]); result = []
        queue.append(root); size = 1;
        while size > 0:
            vec = []; tmp = None;
            for _ in range(size):
                temp = queue.popleft(); size -= 1;
                vec.append(temp.val);
                for i in temp.children:
                    queue.append(i); size += 1;
            result.append(vec);
        return result

