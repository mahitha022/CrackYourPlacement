
    
class Linklist(object):
    def __init__(self):
        self.head=None
        
    class Node(object):
        def __init__(self,d):
            self.val=d
            self.next=None
    
    def push(self,data):
        nn=self.Node(data)
        nn.next=self.head
        self.head=nn
        
    def printList(self):
        t=self.head
        while(t):
            print(t.val,end=" ")
            t=t.next
        print()

    def reorder(self):
        l=[]
        t=self.head
        while(t):
            l.append(t.val)
            t=t.next
        
        i=0
        j=len(l)-1
        c=0
        t=self.head
        while(t):
            if(c%2==0):
                t.val=l[i]
                i+=1
            else:
                t.val=l[j]
                j-=1
            c+=1
            t=t.next
        

ll=Linklist()
#ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.printList()
ll.reorder()
ll.printList()
