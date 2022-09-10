'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

Constraints:

    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.queue = [-1] * k
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.length += 1
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.k
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.length -= 1
            self.queue[self.head] = -1
            self.head = (self.head + 1) % self.k
            return True
        return False

    def Front(self) -> int:
        return self.queue[self.head]

    def Rear(self) -> int:
        return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.k == self.length

# Runtime: 85ms
# Memory: 14.6 MB

# Tests:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1) # True
print(param_1)
param_2 = obj.isFull() # False
print(param_2)
param_3 = obj.deQueue() # True
print(param_3)
param_4 = obj.isFull() # False
print(param_4)

param_5 = obj.enQueue(2) # True
print(param_5)
param_6 = obj.enQueue(3) # True
print(param_6)
param_7 = obj.enQueue(6) # True
print(param_7)
param_8 = obj.isFull() # True
print(param_8)

param_9 = obj.Front()
print(param_9) # 2
param_10 = obj.Rear()
print(param_10) # 6

param_11 = obj.enQueue(7) # False
print(param_11)

param_12 = obj.Front()
print(param_12) # 2
param_13 = obj.Rear()
print(param_13) # 6

param_14 = obj.deQueue() # True
print(param_14)
param_15 = obj.enQueue(7) # True
print(param_15)
param_16 = obj.Rear()
print(param_16) # 7