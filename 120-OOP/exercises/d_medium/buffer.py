class CircularBuffer:  
    def __init__(self, size):
        self.size = size
        self.data_dict = {i: None for i in range(size)}
        self.order = []  # Keeps track of insertion order
        self.data_keys = list(self.data_dict.keys())  # Key rotation
        self.length = size

    def pop_oldest(self):
        if not self.order:
            return None

        idx = self.order.pop(0)
        element = self.data_dict[idx]
        self.data_dict[idx] = None
        return element

    def get(self):
        if set(self.data_dict.values()) == {None}:
            return None 
        return self.pop_oldest()

    def next_index(self):
        idx = self.data_keys.pop(0)
        self.data_keys.append(idx)
        return idx

    def put(self, element):
        idx = self.next_index()
        self.data_dict[idx] = element

        if len(self.order) == self.length:
            self.order.pop(0)
        self.order.append(idx)


# buffer = CircularBuffer(3)

# print(buffer.get() is None)          # True
# print(buffer.data_keys, buffer.order)

# buffer.put(1)
# print(buffer.data_keys, buffer.order)
# buffer.put(2)
# print(buffer.data_keys, buffer.order)
# print(buffer.get() == 1)             # True
# print(buffer.data_keys, buffer.order)

# buffer.put(3)
# print(buffer.data_keys, buffer.order)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)
print(buffer2.data_keys, buffer2.order)
print(buffer2.get() is None)         # True

buffer2.put(1)
print(buffer2.data_keys, buffer2.order)
buffer2.put(2)
print(buffer2.data_keys, buffer2.order)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True