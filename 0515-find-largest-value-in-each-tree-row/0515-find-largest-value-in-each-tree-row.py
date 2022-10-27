# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []; 
        if root:
            queue = [root]; n = 1;
            while(n):
                vector = []; temp = None;
                for i in range(n):
                    temp = queue.pop(0);
                    vector.append(temp.val);
                    if (temp.left): queue.append(temp.left)
                    if (temp.right): queue.append(temp.right)
                result.append(max(vector)); n = len(queue)
        return result