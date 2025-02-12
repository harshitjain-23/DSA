class stack:

    def __init__(self):
        self.itmes = []

    def isempty(self):
        return self.itmes == []

    def push(self, n):
        self.itmes.append(n)
    
    def pop(self):
        if not self.isempty():
            v = self.itmes.pop()
        return v

    def traverse(self):
        for i in range(len(self.itmes)):
            print(self.itmes[i], end=' -->')
        print("None")
        
s = stack()
print(s.isempty())
s.push(8)
s.push(9)
s.push(0)
s.push(5)
s.traverse()
print(s.isempty())
print(s.pop())
s.traverse()