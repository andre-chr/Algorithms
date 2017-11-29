"""
    created by: Andre Christian
    last modified: 29/11/2017
"""

class MinHeap:
    def __init__(self):
        self.array = [None]
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def parent(self, index):
        return index // 2

    def smallest_child(self, k):
        if 2*k == self.count or self.array[2*k] < self.array[2*k+1]:
            return 2*k
        else:
            return 2*k+1

    def sink(self, k):
        while 2*k <= self.count:
            child = self.smallest_child(k)
            if self.array[k] <= self.array[child]:
                break
            self.array[k], self.array[child] = self.array[child], self.array[k]
            k = child

    def serve(self):
        if self.is_empty():
            return None
        #swap root and the last item
        self.array[1], self.array[self.count] = self.array[self.count], self.array[1]
        item = self.array[self.count]
        self.array[self.count] = None
        self.count -= 1
        self.sink(1)
        return item

    def rise(self, k):
        while k > 1 and self.array[k] < self.array[k//2]:
            self.array[k], self.array[k//2] = self.array[k//2], self.array[k]
            k //= 2

    def append(self, item):
        if self.count + 1 < len(self.array):
            self.array[self.count+1] = item
        else:
            self.array.append(item)
        self.count += 1
        self.rise(self.count)


