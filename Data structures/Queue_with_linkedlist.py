class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue (self, n):
        newnode = node(n)

        if self.front is None:
            self.front = newnode
            self.rear = newnode
            return
        else:
            self.rear.next = newnode
            self.rear = newnode
            
        
    def dequeue (self):
        if self.front is None:
            print("List is empty")
            return
        else:
            dequeue_element = self.front.data
            self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeue_element
    
    def show(self):
        if self.front is None:
            print("List is empty")
            return
        else:
            temp = self.front
            while temp:
                print(temp.data, end="<--")
                temp = temp.next
            print("None")
            
        

test = queue()
test.enqueue(8)
test.enqueue(49)
test.show()
print(test.dequeue())
test.show()