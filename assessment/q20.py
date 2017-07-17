k=str(raw_input())
g=k.split()
g.sort()
tuple(g)
for i in range(0,len(g)):
    print(g[i]+":",g.count(g[i]))
