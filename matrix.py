import sys
i=1;

for i in range (1,8):
    j=1;
    print"\n"
    for j in range(1,6):
        if((i==1 and (j==1 or j==5)) or ((i==2 or i==3  or i==5 or i==6 or i==7)and(j==2 or j==3 or j==4))):
            print('  '),
        
            
        else:
            print('* '),
        
       
    

        


