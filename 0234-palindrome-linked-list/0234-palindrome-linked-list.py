# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        
        slow=head
        l.append(slow.val)
        fast=slow.next
        
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
            if(fast):
                
                l.append(slow.val)
            
            
        #for single element [1]
        if(slow.next==None):
            return True
        
        #to check from mid+1 value
        slow=slow.next
        j=len(l)-1

        while(slow):
            if(slow.val!=l[j]):
                return False
            slow=slow.next
            j-=1
        return True