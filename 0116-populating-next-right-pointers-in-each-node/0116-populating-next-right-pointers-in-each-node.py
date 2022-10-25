"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (root):
            queue = [root]; n = 1; root.next = None;
            while(n):
                temp = None;
                for i in range(n):
                    temp = queue.pop(0);
                    if (temp.left):
                        queue.append(temp.left);
                    if (temp.right):
                        queue.append(temp.right);
                n = len(queue);
                for i in range(n-1):
                    queue[i].next = queue[i+1];
        return root