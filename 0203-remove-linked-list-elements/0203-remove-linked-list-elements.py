# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        t=head
        while(t!=None and t.next!=None ):
            
            if(t.next.val==val):
                t.next=t.next.next
            else:
                t=t.next
        if(head and head.val==val):
            return head.next
        return head