import logging
import datetime
def add(b,c):
    return b+c
def sub(b,c):
    return b-c
def mul(b,c):
    return b*c
def div(b,c):
    if (c==0):
        return 'div is not possible'
    else:
        return b/c
def modu(b,c):
    if (c==0):
        return 'remainder doesnt exist'
    else:
        return b%c
i=5
while(i<5):
    print("please enter the operation you want to perform (+ means add),(- means sub),(* means mul),(/ means div),(% means mod)")
    a=str(raw_input())
    if (a!='+' or a!='-'or a!='/'or a!='%'):
         continue;
    else:
         break

try:
    print("please enter the first number")
    b=float(raw_input())
    
except ValueError :
    print("check the number you entered")
       
    
        
print("please enter the second number")
c=float(raw_input())
logging.debug("cannnnnnnnnn")
if (a=='+'):
    x=add(b,c)
    print('your output is', x)
elif (a=='-'):
    x=sub(b,c)
    print('your output is', x)
elif (a=='*'):
    x=mul(b,c)
    print('your output is' ,x)
elif (a=='/'):
    x=div(b,c)
    print('your output is' ,x)
elif (a=='%'):
    x=modu(b,c)
    print('your output is' ,x)
