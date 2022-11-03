# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (root):
            queue = [root]; n = 1;
            while(n):
                vector = []; temp = None;
                for _ in range(n):
                    temp = queue.pop(0);
                    if (temp == None):
                        vector.append(None);
                    else:
                        vector.append(temp.val);
                        queue.append(temp.left);
                        queue.append(temp.right);
                if (vector != vector[::-1]): return False
                del vector; n = len(queue);
        return True
                    