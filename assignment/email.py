k=str(raw_input())
g=list(k)
l=[]
f=g.index('@')
print(f)
o=g.index('.')
for i in range(0,len(g)):
    print(g[i])
    if i>k and i<o:
        l.append( g[i] );
p=''.join(l)
print(l)
print(p)
