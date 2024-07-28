# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        op=ListNode()
        t=op
        carry=0
        while(l1 or l2):
            
            if(l1):
                a=l1.val
            else:
                a=0
            if(l2):
                b=l2.val
            else:
                b=0
            
            total=a+b+carry
            
            value=total%10
            carry=total//10
            
            t.next=ListNode(value)
            t=t.next
            
            if(l1):
                l1=l1.next
            if(l2):
                l2=l2.next
        if(carry):
            t.next=ListNode(carry)
            t=t.next
            
        return op.next