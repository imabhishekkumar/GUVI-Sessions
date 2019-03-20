inp= list(map(int,input().split()))
a=1
for _ in range(max(inp)):
    if a not in inp:
        print(a)
        a=a+1
    else:
        a=a+1