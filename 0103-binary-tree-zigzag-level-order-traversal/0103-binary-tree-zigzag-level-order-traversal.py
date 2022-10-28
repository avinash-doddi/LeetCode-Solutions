# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        fin = []
        if (root):
            queue = [root]; n = len(queue); f = 0;
            while(n):
                temp = None; vector = []
                for i in range(n):
                    temp = queue.pop(0); vector.append(temp.val);
                    if (temp.left): queue.append(temp.left)
                    if (temp.right): queue.append(temp.right);
                if (f):
                    vector.reverse(); fin.append(vector); f = 0; del vector;
                else:
                    fin.append(vector); f = 1; del vector;
                n = len(queue);
        return fin
        