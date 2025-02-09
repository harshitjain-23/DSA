class queue:

    def __init__(self):
        self.items = []

    def isEmpty (self):
        return self.items == []
    
    def enqueue (self, *n):
        self.items.extend(n)
        return

    def dequeue (self):
        if self.isEmpty():
            print("List is empty")
            return
        print(self.items.pop(0))
        return
    
    def size (self):
        print(len(self.items))
        return 
    
    def show (self):
        print("Queue : ", self.items)
        return
    

sample = queue()
print(sample.isEmpty())
sample.size()
sample.enqueue(8,6,9,2)
sample.size()
sample.show()
sample.dequeue()
sample.size()
sample.enqueue(12)
sample.size()
sample.show()


