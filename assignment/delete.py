k=[12,24,35,70,88,120,155]
i=0;
g=[]
while (i<len(k)):
    k.remove(k[i])
    k.insert(i,'')
    
    if i<len(k)-1:
        g.append(k[i+1])
    i=i+2
    
print(g) 

        
