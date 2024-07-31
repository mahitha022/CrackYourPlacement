# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ta,tb=headA,headB
        visit=set()
        
        while(ta or tb):
            if(ta):
                if(ta in visit):
                    return ta
                visit.add(ta)
                ta=ta.next
            if(tb):
                if(tb in visit):
                    return tb
                visit.add(tb)
                tb=tb.next
                
        return None
                