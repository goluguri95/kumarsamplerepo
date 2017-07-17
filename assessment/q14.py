print("enter the positive integer")
k=int(raw_input())
if k==1:
      print("not a power of 2")
else:
    while(k>0):
          if(k%2==0):
              k=k/2
          elif k==1:
              break
        
          else:
              print("not a power of 2")
              break
if k==1:
      print("is a power of 2")


