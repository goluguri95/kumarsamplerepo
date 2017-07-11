import sys
y=float(sys.argv[1])
x=sys.argv[2]

if(x=='c'):
   j=(y*1.8)+32
   print(str(j)+''+' F')
elif(x=='f') :
    j=float(y-32)/1.8
    print(str(j)+''+' c')
  
