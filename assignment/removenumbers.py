k=str(raw_input())
g=list(k)
for i in range(0,len(g)):
    if g[i].isdigit():
       g.remove(g[i])
       g.insert(i,'')
k=''.join(g)
print(k)


