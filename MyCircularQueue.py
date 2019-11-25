class MyCircularQueue:

    def __init__(self, k):
        self.queue = []
        self.size = k

    def enQueue(self, value):
        if len(self.queue) == self.size:
            return False
        self.queue.append(value)
        return True
        

    def deQueue(self):
        if len(self.queue) == 0:
            return False
        else:
            del self.queue[0]
        return True
        
    def Front(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]
        
    def Rear(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[len(self.queue)-1]
        
    def isEmpty(self):
        return len(self.queue) == 0
        
    def isFull(self):
        return len(self.queue) == self.size