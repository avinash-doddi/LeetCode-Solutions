# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []; n = 0
        while head:
            vals.append(head.val); head = head.next; n += 1;
        rtn = [0]*n
        stk = []
        for i in range(n):
            if not stk:
                stk.append(i);
            else:
                if vals[i] > vals[stk[-1]]:
                    while vals[i] > vals[stk[-1]]:
                        ii = stk.pop();
                        rtn[ii] = vals[i];
                        if not stk: break;
                    stk.append(i);
                else:
                    stk.append(i);
        return rtn
                    
        
        