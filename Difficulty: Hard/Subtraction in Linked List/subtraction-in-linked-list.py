#User function Template for python3

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        def length(head):
            c=0
            t=head
            while(t):
                t=t.next
                c+=1
            return c
            
        def reverse(head):
            prev=None
            t=head
            while(t):
                tmp=t.next
                t.next=prev
                prev=t
                t=tmp
            return prev
            
            
            
        op=Node(0)
        opt=op
        sub=False
        
        #check which linked list is bigger
        
        #remove leading zeros
        while(l1 and l1.data==0):
            l1=l1.next
        while(l2 and l2.data==0):
            l2=l2.next
        
        #compare using length
        len1=length(l1)
        len2=length(l2)
        if(len1==0 and len2==0):
            return op
            
        if(len1<len2):
            l1,l2=l2,l1
        
        elif(len1==len2):
            t1=l1
            t2=l2
            while(t1 and t2 and t1.data==t2.data):
                t1=t1.next
                t2=t2.next
            
            #this means both numbers are same resulting a 0
            if(t1==None):
                return op
            if(t1.data<t2.data):
                l1,l2=l2,l1
            
        #reverse them to subtract
        rev1=reverse(l1)
        rev2=reverse(l2)
        
        
        
        while(rev1 and rev2):
            if(sub):
                rev2.data+=1
                sub=False
            if(rev1.data<rev2.data):
                diff=(rev1.data+10)-rev2.data
                opt.next=Node(diff)
                opt=opt.next
                sub=True
            else:
                diff=rev1.data-rev2.data
                opt.next=Node(diff)
                opt=opt.next
            rev1=rev1.next
            rev2=rev2.next
            
        
        while(rev1):
            if(sub):
                rev1.data-=1
                if(rev1.data<0):
                    rev1.data+=10
                else:
                    sub=False
                
            opt.next=Node(rev1.data)
            opt=opt.next
            rev1=rev1.next
                
        
        #reverse the result and remove leading zeros
        oprev=reverse(op.next)
        while(oprev.data==0):
            oprev=oprev.next
        
        return oprev



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends