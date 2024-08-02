"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head==None):
            return
        stack=[head]
        op=Node(0)
        opt=op
        
        while(stack):
            t=stack.pop()
            if(t.next):
                stack.append(t.next)
            if(t.child):
                stack.append(t.child)
            
            
            
            opt.next=t
            t.prev=opt
            t.child=None
            opt=t
        
        op.next.prev=None
        
        return op.next