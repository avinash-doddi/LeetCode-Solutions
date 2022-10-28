# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []; more = []; t = head; c = 0;
        while(t != None):
            if (t.val < x): less.append(t.val);
            else: more.append(t.val);
            c += 1; t = t.next;
        less += more; t = head;
        for i in less:
            t.val = i; t = t.next;
        return head