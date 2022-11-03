# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if (head == None): return head;
        arr = []; temp = head; prev = None;
        while(temp):
            arr.append(temp.val); temp = temp.next;
        temp = head; prev = temp; c = 0
        for i in arr:
            if (i != val):
                temp.val = i; prev = temp; temp = temp.next; c += 1;
        if (c): prev.next = None;
        else: head = None
        return head;
                    
                    