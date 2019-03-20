class stack:
    lis=[]

    def push(self,a):
        self.lis.append(a)
        print(self.lis)

    def pop(self):
        l=len(self.lis)-1
        if(l==-1):
            print("No values to pop")
        else:
            print(self.lis[l])
            self.lis.pop(l) 
            print(self.lis)

 
class imp :
    a= stack()
    
#Pushing to stack
    a.push(1)
    a.push(2)
    a.push(3)
#Popping out from stack
    a.pop()
    a.pop()
    a.pop()
    a.pop()

