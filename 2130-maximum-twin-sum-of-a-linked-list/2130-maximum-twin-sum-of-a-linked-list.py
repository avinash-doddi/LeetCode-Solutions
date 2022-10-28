# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        final = 0
        if (head):
            vector = []; temp = head; n = 0;
            while(temp):
                vector.append(temp.val); n += 1; temp = temp.next;
            i = 0; j = n-1;
            while(i < n//2):
                final = max(final, vector[i]+vector[j]);
                i += 1; j -= 1;
        return final
            