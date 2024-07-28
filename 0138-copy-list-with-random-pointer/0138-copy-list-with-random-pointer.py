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
        t=head
        d={}
        
        op=Node(0)
        opt=op
        
        while(t):
            opt.next=Node(t.val)
            opt=opt.next
            d[t]=[opt,t.random]
            t=t.next
        
       
        t=head
        opt=op.next
        while(opt):
            if(d[t][1]):
                opt.random=d[d[t][1]][0]
            else:
                opt.random=None
            opt=opt.next
            t=t.next
        return op.next