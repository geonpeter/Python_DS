class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [ None for _ in range(self.Max)]
        
    def get_hash(self,k):
        h =0
        for c in k:
            h+=ord(c)  # return the ascii value for each character in the key and adding to h
        return h% self.Max # preparing an index value from hash function
    def __setitem__(self,k,v):
        h = self.get_hash(k)
        self.arr[h]=v
    def __getitem__(self,k):
        h = self.get_hash(k)
        return self.arr[h]
    
    def __delitem__(self,k):
        h = self.get_hash(k)
        self.arr[h]=None
        
if __name__=="__main__":
    t = HashTable()
    t['first_name']='Geon'
    t['last_name']= 'Peter'
    
    print(t['first_name'])