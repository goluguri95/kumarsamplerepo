k=[6,6,12,18,15]
for i in range(0,len(k)-2):
    if (k[i]+k[i+1]==k[i+2]):
        j=k[i+2]
        continue
        
    else:
        print("not an additive sequence")
        break
if j==k[i+2]:
    print("is a additive sequence")


