import sys
i=1;

for i in range(1,7):
     if (i==6):
          for i in range(6, 10):
            print ('* ')*(10-i)
            
     else:
         print('* ')*i
         #i=i+1
     
