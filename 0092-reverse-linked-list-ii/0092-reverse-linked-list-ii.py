# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=[]
        t=head
        c=1
        while(t):
            if(c>=left and c<=right):
                l=[t.val]+l
            c+=1
            t=t.next
            if(c>right):
                break
        
        
        c=1
        t=head
        i=0
        while(t):
            if(c>=left and c<=right):
                t.val=l[i]
                i+=1
            c+=1
            t=t.next
            if(c>right):
                break
        
        return head