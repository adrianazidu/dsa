"""Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.
In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.
Queue operations work as follows:
two pointers FRONT and REAR
FRONT track the first element of the queue
REAR track the last element of the queue
initially, set value of FRONT and REAR to -1
"""

class Queue():

    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1

    def enqueue(self,data):

        if self.tail == self.k - 1:
            print("queue is full")

        elif self.head == -1: #first element
            self.head=0
            self.tail=0
            self.queue[self.tail]=data

        else:
            self.tail = self.tail +1
            self.queue[self.tail]=data

    def dequeue(self):

        if self.head == -1:
            print("Queue is empty")
        
        elif self.head == self.tail: #last element
            savetemp=self.queue[self.head]
            self.head=-1
            self.tail=-1
            return savetemp

        else:
            savetemp=self.queue[self.head] #return element added in the start (head)
            self.head = self.head +1
            return savetemp

    def printqueue(self):
        for i in range(self.head,self.tail +1):
            print(self.queue[i], end=" ")

obj = Queue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printqueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printqueue()
        