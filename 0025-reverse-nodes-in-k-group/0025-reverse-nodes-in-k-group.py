# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []; temp = head; n = 0
        while(temp):
            stack.append(temp.val);
            n += 1; temp = temp.next;
        index = 0; count = 0;
        #print(stack)
        for i in range(n):
            if (count == k):
                stack[index:index+k] = stack[index:index+k][::-1];
                index = i; count = 1;
            else:
                count += 1;
        if (count == k):
            stack[index:index+k] = stack[index:index+k][::-1];
        #print(stack)
        temp = head; i = 0;
        while(temp):
            temp.val = stack[i];
            i += 1; temp = temp.next;
        return head;    
                