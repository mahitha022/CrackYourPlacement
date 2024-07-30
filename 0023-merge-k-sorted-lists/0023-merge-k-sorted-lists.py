# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1,l2):
            
            op=ListNode()
            opt=op
            
            while(l1 and l2):
                
                if(l1.val<l2.val):
                    opt.next=l1
                    l1=l1.next
                
                else:
                    opt.next=l2
                    l2=l2.next
                    
                opt=opt.next
                
            if(l1):
                opt.next=l1
            
            if(l2):
                opt.next=l2
                
            return op.next

                    
        
        if(len(lists)==0):
            return None
        
        while(len(lists)>1):
            l=[]
            for i in range(0,len(lists),2):

                if(i+1<len(lists)):
                    l.append(merge(lists[i],lists[i+1]))
                else:
                    l.append(merge(lists[i],None))
            lists=l
                
        return lists[-1]

