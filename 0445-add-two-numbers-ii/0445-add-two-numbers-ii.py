# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        f=[]
        s=[]
        while(l1 or l2):
            if(l1):
                f.append(l1.val)
                l1=l1.next
            else:
                f=[0]+f
            if(l2):
                s.append(l2.val)
                l2=l2.next
            else:
                s=[0]+s
        
        carry=0
        for i in range(len(f)-1,-1,-1):
            s[i]=s[i]+f[i]+carry
            carry=s[i]//10
            s[i]=s[i]%10
        if(carry):
            s=[carry]+s
            
        op=ListNode()
        t=op
        for value in s:
            t.next=ListNode(value)
            t=t.next
        return op.next
                
        