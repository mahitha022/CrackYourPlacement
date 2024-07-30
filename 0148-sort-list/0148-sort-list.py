# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getmid(head):
            slow=head
            fast=head.next
            while(fast and fast.next):
                slow=slow.next
                fast=fast.next.next
            return slow
        
        def mergeSort(head):
            if(head==None or head.next==None):
                return head

            left=head
            right=getmid(head)
            suc=right.next
            right.next=None
            right=suc

            left=mergeSort(left)
            right=mergeSort(right)

            return merge(left,right)

        

        def merge(left,right):

            op=ListNode()
            opt=op

            while(left and right):

                if(left.val<right.val):
                    opt.next=ListNode(left.val)
                    left=left.next
                else:
                    opt.next=ListNode(right.val)
                    right=right.next

                opt=opt.next

            if(left):
                opt.next=left
            if(right):
                opt.next=right

            return op.next
        
        
        return mergeSort(head)




