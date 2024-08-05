class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        
    def insert(self,newnode):
        pre=self.right.prev
        nex=self.right
        
        pre.next=newnode
        nex.prev=newnode
        newnode.prev=pre
        newnode.next=nex
        
    def delete(self,node):
        p=node.prev
        n=node.next
        
        p.next=n
        n.prev=p        
        

    def get(self, key: int) -> int:
        if(key in self.d):
            self.delete(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        
        if(key in self.d):
            self.delete(self.d[key])
             
        self.d[key]=Node(key,value)
        self.insert(self.d[key])
        if(len(self.d)>self.cap):
            lru=self.left.next
            self.delete(lru)
            del self.d[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)