import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        if(self.head is None):
            self.head = Node(data)
        else:
            pointer = self.head
            while(pointer.next is not None):
                pointer = pointer.next

            pointer.next = Node(data)

    def delete(self, index):
        self.checkEmpty()
        if(index > self.length() or index < 0):
            print("index is out of bounds")
            sys.exit(1)

        if(index == 0):
            self.head = self.head.next
            self.checkEmpty()

        else:
            pointer = self.head
            for i in range(0, index-1):
                pointer = pointer.next

            pointer.next = pointer.next.next


    def length(self):
        self.checkEmpty()
        pointer = self.head
        count = 1
        while(pointer.next is not None):
            count=count+1
            pointer = pointer.next
        return count

    def checkEmpty(self):
        if(self.head is None):
            print("Empty List!")
            sys.exit(1)


    def printList(self):
        pointer = self.head
        while(pointer.next is not None):
            print(pointer.data, end=" ")
            pointer = pointer.next

        print(pointer.data)

myList = LinkedList()
myList.insert(1)
myList.insert(2)
myList.insert(3)
myList.printList()
myList.delete(0)
myList.printList()
