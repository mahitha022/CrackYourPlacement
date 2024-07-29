# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l=[]
        t=head
        while(t):
            l.append(t.val)
            t=t.next
        
        i=0
        j=len(l)-1
        c=0
        t=head
        while(t):
            if(c%2==0):
                t.val=l[i]
                i+=1
            else:
                t.val=l[j]
                j-=1
            c+=1
            t=t.next
        
        return head