"""
    created by: Andre Christian
    last modified: 28/11/2017
"""

class HashTable:
    PRIME_LIST = [
                49157, 98317, 196613, 393241, 786433, 1572869, 3145739,
                6291469, 12582917, 25165843, 50331653, 100663319,
                201326611, 402653189, 805306457, 1610612741
             ]
    def __init__(self):
        self.t_index = 0
        self.count = 0
        self.table_size = self.PRIME_LIST[self.t_index]
        self.array = [None] * self.table_size

    def __len__(self):
        return self.count

    def __iter__(self):
        return iter(self.array)

    def __setitem__(self, key, value):
        return self.insert(key, value)

    def __getitem__(self, key):
        return self.lookup(key)

    def is_full(self):
        return self.count == self.table_size

    def hash(self, key):
        value = 0
        a = 31415
        b = 27183
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.table_size
            a = a * b % (self.table_size - 1)
        return value

    def insert(self, key, item):
        if self.is_full():
            self.resize()
        hash_val = self.hash(key)
        pos = hash_val
        for i in range(self.table_size):
            if self.array[pos] is None:
                self.array[pos] = [key, item]
                self.count += 1
                return self.array[pos][1]
            elif self.array[pos][0] == key:
                self.array[pos][1] = item
                return self.array[pos][1]
            else:
                pos = (hash_val + i**2) % self.table_size
        self.resize()
        self.insert(key, item)

    def lookup(self, key):
        hash_val = self.hash(key)
        pos = hash_val
        for i in range(self.table_size):
            if self.array[pos] is None:
                return None
            elif self.array[pos][0] == key:
                return self.array[pos][1]
            else:
                pos = (hash_val + i**2) % self.table_size
        raise KeyError(key)

    def delete(self, key):
        hash_val = self.hash(key)
        pos = hash_val
        for i in range(self.table_size):
            if self.array[pos] is None:
                return None
            elif self.array[pos][0] == key:
                self.array[pos] = None
                return
            else:
                pos = (hash_val + i**2) % self.table_size
        raise KeyError(key)

    #reinsert items to the table
    def rehash(self):
        old_table = self.array

        self.array = [None] * self.table_size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    #allows the table to be resized when table is full or an item is has failed to insert
    def resize(self):
        if self.t_index < len(self.PRIME_LIST):
            self.t_index += 1
            self.table_size = self.PRIME_LIST[self.t_index]
        else:
            raise RuntimeError('Hash table exceeds capacity!')
        self.rehash()

