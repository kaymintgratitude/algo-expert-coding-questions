# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        for i in reversed(range(len(array))):
            self.siftDown(i, array)
        return array

    def siftDown(self, i, array):
        n = len(array)
        if i < len(array):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n:
                min_child = left
                if right < n and array[right] < array[left]:
                    min_child = right
                if array[min_child] < array[i]:
                    self.swap(min_child, i, array)
                    self.siftDown(min_child, array)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
        return array

    def siftUp(self, i, array):
        if i > 0:
            parent = (i - 1) // 2
            if parent < i and array[i] < array[parent]:
                self.swap(i, parent, array)
                self.siftUp(parent, array)

    def peek(self):
        if self.heap:
            return self.heap[0]

    def remove(self):
        if self.heap:
            n = len(self.heap)
            item = self.heap[0]
            self.heap[0] = self.heap[n - 1]
            self.heap.pop()
            self.siftDown(0, self.heap)
            return item

    def insert(self, value):
        if self.heap:
            n = len(self.heap)
            self.heap.append(value)
            self.siftUp(n - 1, self.heap)
