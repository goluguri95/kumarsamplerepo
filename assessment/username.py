k=str(raw_input())
g=list(k)
l=[]
f=g.index('@')
o=g.index('.')
for i in range(0,len(g)):
    if i<f :
        l.append( g[i] )
p=''.join(l)
print(p)
