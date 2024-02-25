# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        fast = head.next; slow = head
        itr = 0
        while fast and slow and fast.next:
            if fast == slow: 
                return True
            fast = fast.next.next;
            slow = slow.next;
            #itr += 1
        return False
        
        