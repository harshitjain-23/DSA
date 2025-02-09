# Creating a single node
class node:

    def __init__(self, data=None):
        self.data = data
        self.next = None



# Creating a linked list
class linked_list:

    def __init__(self):
        self.head = None

# Adding a node at the beginning
    def insertion_begining(self, data):
        newnode = node(data)

        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode


# Creating a node at last
    def insertion_last(self, data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode


    def insertion_middle(self, data, position):
        newnode = node(data)

        if self.head == None:
            self.head = newnode

        elif position == 1:
            self.insertion_begining(data)
            return

        else:
            n = 1 
            temp = self.head
            while temp is not None and n < position-1:
                n += 1
                temp = temp.next
            if temp is None:
                print("Position out of range")
                return 
            newnode.next = temp.next
            temp.next = newnode


# Deleting first node of linked list
    def delete_first(self):
        if self.head is None:
            print("Empty list")
            return
        else:
            self.head = self.head.next


# Deleting last node of linked list
    def delete_last(self):
        if self.head is None:
            print("Empty list")
            return
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None


# Deleting node from a linked list
    def delete_middle(self, position):
        if self.head is None:
            print("This is the emplty list")
            return
        
        if position == 1:
            self.delete_first()
            return

        temp = self.head
        n = 1
        while temp is not None and n < position-1:
            temp = temp.next
            n += 1
        
        if temp is None:
            print("Position is out of Range")
            return
        
        temp.next = temp.next.next
        

# Searching through a linked list
    def search(self, value):
        if self.head is None:
            print("list is Empty")
            return
        else:
            temp = self.head
            while temp.next:
                if temp.data == value:
                    print("Element Found")
                    return
                temp = temp.next

            print("Element not found")
            return

# Printing the linked list
    def printlist(self):

        if self.head == None:
            print ("Empty list")
            return
        
        temp = self.head
        while temp != None:
            print(temp.data, end=' --> ')
            temp = temp.next
        print("None")
         


# Main Function

l = linked_list()
l.head = node(1)
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)

l.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# l.insertion_beggining(5)
# l.insertion_last(8)
# l.insertion_middle(6,2)

# l.delete_first()
# l.delete_last()
# l.delete_middle(3)

# l.search(6)

l.printlist()


