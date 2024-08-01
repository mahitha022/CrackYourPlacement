
    
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

    def zigzag(self):
        t=self.head
        flag=True
        while(t.next):
            if(flag):
                if(t.val>t.next.val):
                    t.val,t.next.val=t.next.val,t.val
            else:
                if(t.val<t.next.val):
                    t.val,t.next.val=t.next.val,t.val
            if(flag):
                flag=False
            else:
                flag=True
            
            t=t.next
            
        return

ll=Linklist()
ll.push(10)
ll.push(5)
ll.push(20)
ll.push(15)
ll.push(11)
ll.printList()
ll.zigzag()
ll.printList()
