class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [-1]*k
        self.front = 0 # really pointed at the front element in the queue
        self.rear = 0 # pointed to the next position of the rear element

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear%self.k] = value
        self.rear += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front%self.k] = -1
        self.front+=1
        return True

    def Front(self) -> int:
        return self.q[self.front%self.k]

    def Rear(self) -> int:
        return self.q[(self.rear - 1)%self.k]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.rear - self.front == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
