# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #level Order traversal
        level = -inf; curr_max = -inf; lvl = 1
        queue = [root]; n = 1; count = 1;
        while (n > 0):
            vector = [];
            for i in range(n):
                temp = queue.pop(0);
                vector.append(temp.val);
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            n = len(queue);
            if sum(vector) > curr_max:
                level = lvl; curr_max = sum(vector);
            lvl += 1
        return level
                
        