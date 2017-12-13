import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def checkEmpty(self):
        if(self.root is None):
            print("The BST is empty!")
            sys.exit(1)


    def insert(self, value):

        if(self.root is None):
            self.root = Node(value)

        else:
            pointer = self.root

            while(True):
                if(value <= pointer.value):
                    if(pointer.left is not None):
                        pointer = pointer.left

                    else:
                        pointer.left = Node(value)
                        break

                if(value > pointer.value):
                    if(pointer.right is not None):
                        pointer = pointer.right

                    else:
                        pointer.right = Node(value)
                        break

    def findValue(self, value):
        if(self.root == None):
            return "NOT FOUND"

        pointer = self.root

        while(True):
            if(value < pointer.value):
                if(pointer.left is not None):
                    pointer = pointer.left

                else:
                    break

            if(value > pointer.value):
                if(pointer.right is not None):
                    pointer = pointer.right

                else:
                    break

            if(value == pointer.value):
                return "FOUND"

        return "NOT FOUND"

    def inOrderTraversal(self):
        self.checkEmpty()
        treeList = []
        self.inOrderHelper(self.root, treeList)
        print(*treeList)

    def inOrderHelper(self, pointer, treeList):

        if(pointer.left):
            self.inOrderHelper(pointer.left, treeList)

        treeList.append(pointer.value)

        if(pointer.right):
            self.inOrderHelper(pointer.right, treeList)




    def levelOrderTraversal(self):
        self.checkEmpty()

        pointer = self.root
        treeList = []

        self.levelOrderTraversalHelper(pointer, treeList)
        treeList.append(pointer.value)
        treeList.reverse()

        for level in treeList:
            if type(level) is not  int:
                print(*level) #Prints all elements in list
            else:
                print(level)

    def levelOrderTraversalHelper(self, pointer, treeList):
        thisLevel = []

        if(pointer.left):

            thisLevel.append(pointer.left.value)
            self.levelOrderTraversalHelper(pointer.left, treeList)
        if(pointer.right):

            thisLevel.append(pointer.right.value)
            self.levelOrderTraversalHelper(pointer.right, treeList)

        if(len(thisLevel) > 0):
            treeList.append(thisLevel)


print("-----Inserting Values-----")
myBST = BST()
print("Inserting 2")
myBST.insert(2)
print("Inserting 1")
myBST.insert(1)
print("Inserting 3")
myBST.insert(3)
print("Inserting 5")
myBST.insert(5)
print("Inserting 4")
myBST.insert(4)
print("Inserting 6")
myBST.insert(6)
print("-----Level Order Traversal-----")
myBST.levelOrderTraversal()
print("-----Finding a value-----")
print("4 Found?", myBST.findValue(4))
print("7 Found?:", myBST.findValue(7))
print("-----In Order Traversal-----")
myBST.inOrderTraversal()
