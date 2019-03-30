class node:
    def __init__(self,value):
        self.value=value
        self.leftChild=None
        self.rightChild=None
        self.totalChild=0

class binaryTree:
        def __init__(self):
            self.rootVal=None

        def insertLeft(self, val):
            rootNode=self.rootVal
            if(rootNode.leftChild is  None):
                self.rootVal.leftChild=val
            else:
                print("Left Child Full")
                #self.totalChild=self.totalChild+1

        def insertRight(self, val):
            rootNode=self.rootVal
            if(rootNode.rightChild is None):
                self.rootVal.rightChild=val
            else:
                 print("Right Child Full")
               # self.totalChild=self.totalChild+1

        def addNode(self,value):
            self.rootVal=node(value)
        
        def printNode(self):
            printVal=self.rootVal
            if printVal is not None:
                print(printVal.value)
                if(printVal.leftChild is not None):
                    print(printVal.leftChild)
                
                if(printVal.rightChild is not None):
                    print(printVal.rightChild)
               
            


        


nodeVal=int(input("Enter root node: "))
bt=binaryTree()
bt.addNode(nodeVal)

insertVal=int(input("Enter insert val: "))

if insertVal<nodeVal:
    bt.insertLeft(insertVal)
else:
    bt.insertRight(insertVal)


insertVal=int(input("Enter insert val: "))

if insertVal<nodeVal:
    bt.insertLeft(insertVal)
else:
    bt.insertRight(insertVal)

bt.printNode()