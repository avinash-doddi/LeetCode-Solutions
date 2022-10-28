# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []; t = list1;
        while(t != None):
            arr.append(t.val);
            t = t.next;
        t = list2;
        while(t != None):
            arr.append(t.val);
            t = t.next;
        arr.sort(); n = len(arr); new = None; i = 0;
        while(n > i):
            if (new == None):
                new = ListNode(); new.val = arr[i]; i += 1; t = new;
            else:
                t.next = ListNode(); t = t.next;
                t.val = arr[i]; i += 1;
        return new
        
        