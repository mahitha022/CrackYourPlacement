# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n=0
        t=head
        while(t!=None):
            n+=1
            t=t.next
        mid=(n//2)+1
        n=0
        t=head
        while(t!=None):
            n+=1
            if(n==mid):
                return t
            t=t.next
        

        