
import sys
import re
def validate(p):    
    x = True
    while x:  
        if (len(p)<6 or len(p)>12):
            break
        elif not re.search("[a-z]",p):
            break
        elif not re.search("[A-Z]",p):
            break
        elif not re.search("[$#@]",p):
            break
        elif not re.search("[0-9]",p):
            break
        else:
            return ("Valid")
    if(x):
        return "Not Valid"
print validate(raw_input())
