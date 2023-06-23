from collections import deque;
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minSwap(self, arr, n):
	    ans = 0;
	    temp = arr.copy()
	    h = {}; temp.sort()
	    for i in range(n):
		    h[arr[i]] = i
	    init = 0
	    for i in range(n):
		    if (arr[i] != temp[i]):
			    ans += 1
			    init = arr[i]
			    arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i];
			    h[init] = h[temp[i]]
			    h[temp[i]] = i	
	    return ans

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def is_sorted(arr, n):
            for i in range(n-1):
                if (arr[i] > arr[i+1]): return False
            return True;           
        
        queue = deque([root]); n = 1; oper = 0;
        while(n):
            vect = []; temp = None; count = 0;
            for i in range(n):
                temp = queue.popleft();
                vect.append(temp.val); count += 1;
                if (temp.left): queue.append(temp.left);
                if (temp.right): queue.append(temp.right);
            if (count > 1):
                if (not is_sorted(vect, count)): 
                    oper += self.minSwap(vect, count);
            print(vect, oper)
            del vect; n = len(queue)
        return oper
            