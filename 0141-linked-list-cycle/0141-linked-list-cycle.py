# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d={}
        t=head
        while(t!=None):
            if(t in d):
                return True
            d[t]=t.val
            t=t.next
        return False
            