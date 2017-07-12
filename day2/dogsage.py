import sys
i=int(sys.argv[1])
if (i<=2):
    k=k*10.5
    print('The dogs age in dogs years is'+ str( k))
else:
    k=2*10.5+(i-2)*4
    print('The dogs age in dogs years is'+ str( k))
    
