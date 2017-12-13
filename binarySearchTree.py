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

    def levelOrderTraversal(self):
        self.checkEmpty()

        pointer = self.root
        treeList = []

        self.levelOrderTraversalHelper(pointer, treeList)
        treeList.append(pointer.value)
        treeList.reverse()
        print(treeList)

    def levelOrderTraversalHelper(self, pointer, treeList):
        thisLevel = []

        if(pointer.left):
            # print("Left Child:", pointer.left.value)
            thisLevel.append(pointer.left.value)
            self.levelOrderTraversalHelper(pointer.left, treeList)
        if(pointer.right):
            # print("Right Child:", pointer.right.value)
            thisLevel.append(pointer.right.value)
            self.levelOrderTraversalHelper(pointer.right, treeList)

        if(len(thisLevel) > 0):
            treeList.append(thisLevel)


myBST = BST()
myBST.insert(2)
myBST.insert(1)
myBST.insert(3)
myBST.insert(5)
myBST.insert(4)
myBST.insert(6)
myBST.levelOrderTraversal()
