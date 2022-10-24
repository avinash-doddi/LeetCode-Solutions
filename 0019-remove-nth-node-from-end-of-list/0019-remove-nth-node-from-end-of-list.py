# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head; temp1 = head; count = 0;
        while (temp != None):
            temp = temp.next;
            count += 1;
        if (n >= 1 and count == 1): return None;
        rem = count - n - 1; rem2 = count - n + 1; temp = head;
        if (rem2 == 1): 
            head = head.next;
            return head;
        while(rem > 0):
            temp = temp.next; rem -= 1;
        while(rem2 > 0):
            temp1 = temp1.next; rem2 -= 1;
        temp.next = temp1;
        return head;
        