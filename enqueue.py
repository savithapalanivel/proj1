class queue:
    def __init__(self):
        self.queue=list()
    def enqueue(self,data):
        self.queue.insert(data)
    def dequeue(self):
        if len(self.queue)>0:
            self.queue.pop()
        return ("Queue Empty!")
    def size(self):
        return len(self.queue)
    def printqueue(self):
        return self.queue
q=queue()
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(9))
print(q.enqueue(5))
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
