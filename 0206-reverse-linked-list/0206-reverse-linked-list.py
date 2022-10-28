# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None): return head;
        count = 0; arr = []; t = head;
        while(t != None):
            count += 1; arr.append(t.val); t = t.next;
        if (count == 1): return head;
        arr.reverse(); t = head;
        for i in arr:
            t.val = i; t = t.next;
        return head