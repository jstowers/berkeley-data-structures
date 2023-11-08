class HashTable:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.array = [ None ] * self.capacity
        self.count = 0
        
    def hash_function(self, key):
        charsum = sum(ord(c) * i for i, c in enumerate(key, 1))
        return charsum % self.capacity      
        
    def key_exists(self, key):
        bucket = self.hash_function(key)
        if self.array[bucket] is None:
            return False
        
        for e in self.array[bucket]:
            if e[0] == key:
                return True
        return False

    def add(self, key, value):
        bucket = self.hash_function(key)
        if self.array[bucket] is None:
            self.array[bucket] = [ [key, value] ]
        else:
            self.array[bucket].append([ key, value ])

        self.count += 1

    def set(self, key, value):
        bucket = self.hash_function(key)

        for e in self.array[bucket]:
            if e[0] == key:
                e[1] = value

    def get(self, key):
        bucket = self.hash_function(key)

        if self.array[bucket] is None:
            return None
        
        for e in self.array[bucket]:
            if e[0] == key:
                return e[1]

        return None

    def delete(self, key):
        bucket = self.hash_function(key)
        if self.array[bucket]:
            for i in range(len(self.array[bucket])):
                if self.array[bucket][i][0] == key:
                    del self.array[bucket][i]
                    if len(self.array[bucket]) ==  0:
                        self.array[bucket] = None
                    self.count -= 1
                    break

    def size(self):
        return self.count
    
    def __repr__(self):
        s = ""
        for i, bucket in enumerate(self.array):
            s += f"Bucket {i}: {bucket}\n"
        return s

