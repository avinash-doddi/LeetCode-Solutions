# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0; temp = head;
        while(temp != None):
            count += 1;
            temp = temp.next;
        if (count == 1):
            return head;
        if (count == 2):
            head = head.next;
            return head;
        n = (count//2);
        while(n > 0):
            head = head.next;
            n -= 1;
        return head
        