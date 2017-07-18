
sum=0
while True:
    j=str(raw_input())
    if not j:
        break
    b=j.split()
    if (b[0]=='D'):
        sum=sum+int(b[1])
    if (b[0]=='W'):
        sum=sum-int(b[1])
    
print(sum)
