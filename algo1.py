class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hash_table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError("Key not found")

    def delete(self, key):
        index = self._hash_function(key)
        for pair in self.hash_table[index]:
            if pair[0] == key:
                self.hash_table[index].remove(pair)
                return
        raise KeyError("Key not found")


