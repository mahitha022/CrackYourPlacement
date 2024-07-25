# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        t=head
        s=""
        while(t!=None):
            s+=str(t.val)
            t=t.next
        
        digit=0
        n=len(s)-1
        for i in range(len(s)):
            if(s[i]=='1'):
                digit+=(2**n)
            n-=1
        return digit
            