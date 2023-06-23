# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        from collections import deque as dq, defaultdict as maps
        queue = dq([]); mp = maps(list);
        row, col = 0,0;
        queue.append((root, row, col)); size = 1;
        while size > 0:
            node, row, col = queue.popleft(); size -= 1;
            mp[col].append((node.val, row))
            if node.right:
                queue.append((node.right, row + 1, col + 1));
                size += 1;
            if node.left:
                queue.append((node.left, row + 1, col - 1));
                size += 1;
        tmp = list(mp.keys()); tmp.sort()
        finalarr = []
        for col in tmp:
            col_vals = mp[col];
            col_vals.sort(key = lambda x: (x[1], x[0]))
            finalarr.append([vals[0] for vals in col_vals])
        return finalarr
        
        
            


