# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vector = []; temp = head;
        while(temp):
            vector.append(temp.val); temp = temp.next;
        vector.sort(); i = 0; temp = head
        while(temp):
            temp.val = vector[i]; i += 1; temp = temp.next;
        return head