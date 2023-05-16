# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []; c = 0; t = head;
        while(t != None):
            arr.append(t.val); c += 1; t = t.next;
        s1 = k - 1; s2 = c - k;
        arr[s1], arr[s2] = arr[s2], arr[s1]; t = head; i = 0;
        while(t != None):
            t.val = arr[i]; i += 1; t = t.next;
        return head