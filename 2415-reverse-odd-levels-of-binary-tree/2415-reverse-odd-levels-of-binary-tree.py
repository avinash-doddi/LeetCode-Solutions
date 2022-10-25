# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root):
            queue = [root]; n = 1; level = -1;
            while(n > 0):
                vector = []; temp = None; level += 1; remember = []
                for i in range(n):
                    temp = queue.pop(0); vector.append(temp.val);
                    remember.append(temp)
                    if (temp.left): queue.append(temp.left);
                    if (temp.right): queue.append(temp.right);
                if (level & 1):
                    vector.reverse()
                    for i in range(len(vector)):
                        remember[i].val = vector[i];
                del remember; del vector;
                n = len(queue)
        return root
                    