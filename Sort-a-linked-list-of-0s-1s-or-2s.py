class Linklist(object):
    def __init__(self):
        self.head=None
    
    class Node(object):
        def __init__(self,data):
            self.val=data
            self.next=None
    
    def push(self,data):
        
        new= self.Node(data)
        new.next=self.head
        self.head=new

    
    def printLink(self):
        
        t=self.head
        while(t!=None):
            print(t.val,end=" ")
            t=t.next
        print()
            
    def SortLink(self):
        d={}
        t=self.head
        while(t!=None):
            d[t.val]=d.get(t.val,0)+1
            t=t.next
        t=self.head
        i=0
        while(t!=None):
            if(d[i]==0):
                i+=1
            t.val=i
            d[i]-=1
            t=t.next
        return
        
ll=Linklist()
ll.push(0)
ll.push(2)
ll.push(1)
ll.push(0)
ll.push(1)
ll.push(1)
ll.push(2)
ll.printLink()

ll.SortLink()
ll.printLink()
