class node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, data):
        if self.isempty() == True:
            self.top = node(data)
            return
        temp = node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isempty() == True:
            return "List is empty nothing to remove"
        temp = self.top.data
        self.top = self.top.next
        return temp
    
    def show(self):
        if self.isempty() == True:
            print("List is empty nothing to print")
            return
        temp = self.top
        while temp != None:
            print(temp.data, end=' <--  ')
            temp = temp.next
        print("None")

s = stack()
print(s.isempty())
s.push(5)
s.push(6)
s.push(2)
s.push(0)
s.show()
print(s.isempty())
print(s.pop())
s.show()
