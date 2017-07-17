tup=(1,2,3,4,5,6,7,8,9,10)
a=list(tup)
l=[]
for i in range(0,10):
    if i%2!=0:
        l.append(a[i])
k=tuple(l)
print(k)
