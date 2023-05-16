# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None
        if (head):
            temp = head; temp2 = head.next; temp3 = None;
            while(temp != None and temp2 != None):
                if (temp3): temp3.next = temp2;
                temp.next = temp2.next;
                temp2.next = temp;
                if (newhead == None):
                    newhead = temp2;
                temp3 = temp;
                temp = temp.next
                if (temp):                
                    temp2 = temp.next;
        if (newhead): return newhead;
        return head