class RandomizedCollection:

    def __init__(self):
        self.d=defaultdict(set)
        self.l=[]
        

    def insert(self, val: int) -> bool:
        if(val in self.d and len(self.d[val])>0):
            x=False
        else:
            x=True
        self.d[val].add(len(self.l))
        self.l.append(val)
        return x          
        

    def remove(self, val: int) -> bool:
        if(val in self.d and len(self.d[val])>0):
            dict_pos=self.d[val].pop()
            last_list_pos=len(self.l)-1
            last_list_ele=self.l[last_list_pos]
            
            self.d[last_list_ele].add(dict_pos)
            self.d[last_list_ele].remove(last_list_pos)
            
            
            self.l[dict_pos]=self.l[last_list_pos]
            self.l.pop()
            
            return True
        return False
                   

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


    