class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, data):
        position = self.hash(key)
        if self.slots[position] is None:
            self.slots[position], self.data[position] = key, data
        elif self.slots[position] == key:
            self.data[position] = data
        else:
            reposition = self.rehash(key, position)
            while self.slots[reposition] is not None and self.slots[reposition] != key:
                reposition = self.rehash(key, reposition)

            if self.slots[reposition] is None:
                self.slots[reposition], self.data[reposition] = key, data
            else:
                self.data[reposition] = data

            
    def hash(self, key):
        return key % self.size
    
    
    def rehash(self, key, reposition):
        return (reposition + 1) % self.size

    
    def get(self, key):
        position = self.hash(key)
        if self.slots[position] is None:
            return False
        elif self.slots[position] == key:
            return self.data[position]
        else:
            reposition = self.rehash(key, position)
            while self.slots[reposition] is not None and self.slots[reposition] != key and reposition != position:
                reposition = self.rehash(key, reposition)

            if self.slots[reposition] == key:
                return self.data[reposition]
            else:
                return False


    def delete_(self, key):
        position = self.hash(key)
        if self.slots[position] is None:
            return False
        elif self.slots[position] == key:
            del self.slots[position], self.data[position]
        else:
            reposition = self.rehash(key, position)
            while self.slots[reposition] is not None and self.slots[reposition] != key and reposition != position:
                reposition = self.rehash(key, reposition)

            if self.slots[reposition] == key:
                del self.slots[reposition], self.data[reposition]
            else:
                return False
  

    
        
    def __getitem__(self, key):
        return self.get(key)
    

    def __setitem__(self, key, data):
        self.put(key, data)


