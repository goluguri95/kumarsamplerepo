k=[12,24,35,24,88,120,155,88,120,155]
g=[]
for i in range (0,len(k)):
    
    for j in range(i+1,len(k)):
        if k[i]==k[j] and k[i]!='':
            k.remove(k[i])
            k.insert(i,'')
    if k[i]!='':
        g.append(k[i])
g.reverse()
print(g)
            
        
