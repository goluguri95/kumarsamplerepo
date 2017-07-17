i=[1,2,3,4,6,7,8]
for j in range(0,len(i)-1):
    if ((i[j+1]-i[j])==2):
        print(i[j+1]-1)
