k=[12,24,35,24,88,120,155,88,120,155]
g=[]
for i in range (0,len(k)):
    p=i+1
    for j in range(p,len(k)):
        if (k[j]==k[i] and k[i]!=''):
            k.remove(k[i])
            k.insert(i,'')
    if k[i]!='':
        g.append(k[i])


print(g)
            
        
