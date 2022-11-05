# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}; fin = None
        temp = head;
        while(temp != None):
            if (temp in visited):
                fin = temp; break;
            else: visited[temp] = 1;
            temp = temp.next;
        return fin;