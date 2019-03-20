class string:
    

    def copy(self,inp):
        return "".join(inp)


    def rev(self,inp):
        revInp=[]
        l=len(inp)
        last=l-1
        
        for i in range(l):
            revInp.append(inp[last])
            last=last-1

        return "".join(revInp)


class test:
    inp= list(input("Enter String: "))
    m= string()

    str1=m.copy(inp)
    str2=m.rev(inp)

    print("Copied string: "+str1)
    print("Reversed string: " + str2)
