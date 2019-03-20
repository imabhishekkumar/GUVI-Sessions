

class node:
    def __init__(self,value=None):
        self.value=value
        self.nextVal=None


class linkedList:
    i=0
    def __init__(self):
        self.rootVal=None

    def printNode(self):
        printVal=self.rootVal
        while printVal is not None:
            print(printVal.value)
            printVal=printVal.nextVal

    def del_node(self,value):
        delVal=self.rootVal
        pre = node()
        if delVal.value == value:
            self.rootVal=delVal.nextVal
            return
        else:
            while delVal.nextVal is not None:
                if delVal.value==value:
                    pre.nextVal=delVal.nextVal
                    break
                else:
                    pre = delVal
                    delVal=delVal.nextVal


    def addnode(self,nodeVal):
        if(self.i==0):
            self.rootVal.nextVal=nodeVal
            self.i=self.i+1
        else:
            self.rootVal=node(nodeVal)





class main:
    

    ll=linkedList()
    


    


    rootNode= input("Enter root node: ")
    ll.rootVal=node(rootNode)
    
    e1=node(20)
    e2=node(30)
    e3=node(44)
    e4=node(55)
    e5=node(60)


    ll.rootVal.nextVal=e1
    e1.nextVal=e2
    e2.nextVal=e3
    e3.nextVal=e4
    e4.nextVal=e5
    ll.printNode()
    toDel= int(input("Enter Value to delete: "))
    ll.del_node(toDel)
    ll.printNode()




    
