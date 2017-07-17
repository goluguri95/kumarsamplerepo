k=str(raw_input())
g=list(k)
sum=0
nsum=0
for i in range(0,len(g)):
    if g[i].isdigit():
        sum=sum+1
    elif g[i].isalpha():
        nsum=nsum+1
    else:
        continue
print('letters ' ,nsum)
print('digits ' ,sum)
