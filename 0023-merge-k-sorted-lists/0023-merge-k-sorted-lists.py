# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = None; s = []
        for i in lists:
            temp = i;
            while(temp != None):
                s.append(temp.val); temp = temp.next;
        s.sort()
        if (len(s) == 0): return None;
        head = ListNode(s[0]); temp = head;
        for i in range(1,len(s)):
            temp.next = ListNode(s[i]);
            temp = temp.next;
        return head
       
        