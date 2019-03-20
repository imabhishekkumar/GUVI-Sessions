def reverseString(s):
    l=len(s)
    if l==0:
        return s
    else:
         return reverseString(s[1:])+s[0]
print(reverseString("Abhishek Kumar"))

    
    