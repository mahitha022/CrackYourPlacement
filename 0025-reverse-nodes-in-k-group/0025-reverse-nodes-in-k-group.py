# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def getk(t,k):
            while(t and k>0):
                t=t.next
                k-=1
            return t
            
        op=ListNode()
        
        groupprev=op
        groupprev.next=head
        
        while(True):
            kth = getk(groupprev,k)
            
            if(kth==None ):
                break
            groupnext=kth.next
            prev=kth.next
            cur=groupprev.next
            
            while(cur!=groupnext):
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            
            nextKthDummy=groupprev.next
            groupprev.next=kth
            groupprev=nextKthDummy
            
        return op.next
            
                