# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict as mp;
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head):
            curr = None; temp = head;
            while(temp):
                curr = temp;
                if (temp):
                    while(temp.val == curr.val):
                        temp = temp.next;
                        if (temp == None): break;
                    curr.next = temp;
        return head;
                    