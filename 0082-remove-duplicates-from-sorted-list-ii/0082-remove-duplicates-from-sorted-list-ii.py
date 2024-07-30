# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        op=ListNode()
        opt=op
        
        opt.next=head
        
        while(opt):
            
            if(opt.next and opt.next.next and opt.next.val==opt.next.next.val):
                
                temp=opt.next.next
                
                while(temp and temp.next and temp.val==temp.next.val):
                    temp=temp.next
                
                opt.next=temp.next
                
            
            else:
                opt=opt.next
                
        return op.next