
    
class Linklist:
    def __init__(self,d):
        self.head=None
        self.val=d
        self.next=None
    
    def push(self,data):
        nn=Linklist(data)
        nn.next=self.head
        self.head=nn
        
    def printList(self,):
        t=self.head
        while(t):
            print(t.val,end=" ")
            t=t.next
        print()

    def evenodd(self):
        op=Linklist(0)
        opt=op
        
        t=self.head

        while(t):
            if(t.val%2==0):
                opt.next=Linklist(t.val)
                opt=opt.next

            t=t.next
            
        t=self.head
        while(t):
            if(t.val%2!=0):
                opt.next=Linklist(t.val)
                opt=opt.next
            t=t.next
            
        self.head=op.next
        return 
        

ll=Linklist(0)
ll.push(10)
ll.push(5)
ll.push(20)
ll.push(15)
ll.push(11)
ll.printList()
ll.evenodd()
ll.printList()
