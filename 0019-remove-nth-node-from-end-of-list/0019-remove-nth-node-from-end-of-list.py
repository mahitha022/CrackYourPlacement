# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        t=head
        while(t):
            length+=1
            t=t.next
        
        if(length==1 and n==1):
            return None
        
        remove=length-n
        if(remove==0):
            return head.next
        i=0
        t=head
        while(t):
            if(i==remove-1):
                t.next=t.next.next
           
                break
            t=t.next
            i+=1
        
        return head