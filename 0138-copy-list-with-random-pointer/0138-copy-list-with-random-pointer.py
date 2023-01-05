"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        maps = {}; count = {}; temp = head; c = 0
        while(temp):
            count[temp] = c;
            maps[c] = temp.random; c += 1; temp = temp.next;
        for i in maps.keys():
            if maps[i]:
                maps[i] = count[maps[i]];
        print(maps);count = {};
        #create new linked list
        node = None; temp = head; temp1 = None; c = 0;
        while (temp):
            if node:
                temp1.next = Node(temp.val)
                temp1 = temp1.next; temp = temp.next;
                count[c] = temp1; c += 1;
            else:
                node = Node(temp.val); temp1 = node; 
                count[c] = temp1; c += 1; temp = temp.next;
        temp = node; c = 0; print(count);
        while(temp):
            if maps[c] != None:
                print(count[maps[c]])
                temp.random = count[maps[c]];
                print(temp.random.val)
            c += 1; temp = temp.next;
        return node
            
                

        