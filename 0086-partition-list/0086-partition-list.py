# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=[]
        great=[]
        
        t=head
        while(t):
            if(t.val<x):
                less.append(t.val)
            else:
                great.append(t.val)
            
            t=t.next
        
        t=head
        
        for v in less+great:
            t.val=v
            t=t.next
        
        return head