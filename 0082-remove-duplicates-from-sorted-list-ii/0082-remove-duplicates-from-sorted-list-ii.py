# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict as mp
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []; t = head; d = mp(int); c = 0
        while(t != None):
            d[t.val] += 1; t = t.next;
        new = None; t = None;
        for i in sorted(d.keys()):
            if (d[i] == 1):
                if (new == None):
                    new = ListNode(); new.val = i; t = new;
                else:
                    t.next = ListNode(); t = t.next; t.val = i;
        return new;