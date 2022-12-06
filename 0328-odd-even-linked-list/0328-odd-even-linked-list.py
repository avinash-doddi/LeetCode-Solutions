# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []; odd = []; temp = head; index = 0;
        if (head == None): return head;
        while(temp != None):
            index += 1;
            odd.append(temp.val) if index&1 else even.append(temp.val);
            temp = temp.next;
        resultant_array = odd + even; newhead = None; temp = None;
        del even; del odd; del index;
        for i in resultant_array:
            if (newhead == None):
                newhead = ListNode(i);
                temp = newhead;
            else:
                temp.next = ListNode(i);  temp = temp.next;
        del resultant_array;
        return newhead;
            