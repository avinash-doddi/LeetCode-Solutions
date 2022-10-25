# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0;
        count1 = 0; count2 = 0; temp1 = l1; temp2 = l2; vall = 0;
        while(temp1 != None):
            count1 += 1;
            temp1 = temp1.next;
        while(temp2 != None):
            count2 += 1;
            temp2 = temp2.next;
        temp1 = l1; temp2 = l2;
        if (count1 > count2):
            while (count1 > 0):
                if (count2 > 0):
                    vall = temp1.val + temp2.val + carry;
                    carry = vall//10; vall = vall%10;
                    temp1.val = vall; count1 -= 1; count2 -= 1;
                    temp1 = temp1.next; temp2 = temp2.next;
                else:
                    if (carry > 0):
                        vall = temp1.val + carry;
                        carry = vall//10; vall = vall%10;
                        temp1.val = vall; count1 -= 1; 
                        if (count1 == 0 and carry > 0):
                            temp1.next = ListNode(); temp1.next.val = carry;
                        else: temp1 = temp1.next;
                    else: return l1
            return l1;
        else:
            while (count2 > 0):
                if (count1 > 0):
                    vall = temp1.val + temp2.val + carry;
                    carry = vall//10; vall = vall%10;
                    temp2.val = vall; count1 -= 1; count2 -= 1;
                    if (count2 == 0  and carry > 0):
                        temp2.next = ListNode(); temp2.next.val = carry;
                    else: 
                        temp2 = temp2.next; temp1 = temp1.next;
                else:
                    if (carry > 0):
                        vall = temp2.val + carry;
                        carry = vall//10; vall = vall%10;
                        temp2.val = vall; count2 -= 1;
                        if (count2 == 0  and carry > 0):
                            temp2.next = ListNode(); temp2.next.val = carry;
                        else: temp2 = temp2.next
                    else: return l2
            return l2;          
                
                