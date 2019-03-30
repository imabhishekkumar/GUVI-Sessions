inp= list(map(int,input().split()))
unique= list(set(inp))
for i in unique:
    for j in inp:
        if i == j:
            inp.remove(j)
print(inp)