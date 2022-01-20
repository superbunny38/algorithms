from priority_queue_base import *
from PositionalList import *
class Empty(Exception):
    pass

class HeapPriorityQueue(PriorityQueueBase):#base class defines _Item
    """ A min-oriented priority queue implemented with a binary headp."""
    #--------------nonpublic behaviors-----------------
    def _parent(self,j):
        return (j-1)//2

    def _left(self,j):
        return 2*j+1

    def _right(self,j):
        return 2*j+2

    def _has_left(self,j):
        return self._left(j) <len(self._data)

    def _has_right(self,j):
        return self._right(j) < len(self._data)

    def _swap(self,i,j):
        """Swap the elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j>0 and self._data[j]._key < self._data[parent]._key:
            self._swap(j,parent)
            self._upheap(parent)#recur at position of parent

    def _downheap(self,j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            
            if self._has_right(j):
                right = self._right(j)
                if self._data[right]._key<self._data[left]._key:
                    small_child = right
            if self._data[small_child]._key < self._data[j]._key:
                self._swap(j,small_child)
                self._downheap(small_child)
                
    def _heapify(self):
        start = self._parent(len(self)-1)#start at parent of last leaf
        for j in range(start,-1,-1):#going to and including the root
            self._downheap(j)

    def traverse(self):
        for d in self._data:
            print("key:{} value: {}".format(d._key, d._value))
        return self._data


    def __init__(self, contents = ()):
        """Create a new empty Priority QUeue."""
        #self._data = PositionalList()
        self._data = [self._Item(k,v) for k,v in contents]
        if len(self._data)>1:
            self._heapify()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)#upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self._swap(0,len(self._data)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)





HPQ = HeapPriorityQueue()
for i in range(10):
    HPQ.add(10-i,"A"+str(i))
HPQ.traverse()
print("\n\nHeapify")
HPQ._heapify()
HPQ.traverse()

HPQ.display()











        
            
