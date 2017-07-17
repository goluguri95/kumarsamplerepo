k=int(raw_input())
sum=0
for i in range(0,k):
    j=str(raw_input())
    b=j.split()
    if (b[0]=='D'):
        sum=sum+int(b[1])
    if (b[0]=='W'):
        sum=sum-int(b[1])
    
print(sum)
