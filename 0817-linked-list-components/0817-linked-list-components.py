# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        cnt = 0;  ll = []; n = 0
        while head:
            ll.append(head.val); head = head.next; n += 1;
        nums = set(nums); temp = 0;
        for i in range(n):
            if ll[i] in nums:
                temp = 1;
            else:
                if temp:
                    #print("enterr", ll[i])
                    cnt += 1; temp = 0;
        if temp: cnt += 1;
        return cnt
                
                