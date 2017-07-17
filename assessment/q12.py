import logging

k=[6,6,12,18,15]
logging.basicConfig(filename='q12.log' ,level=logging.DEBUG)
for i in range(0,len(k)-2):
    logging.debug("can be a souce of error")
    if (k[i]+k[i+1]==k[i+2]):
        j=k[i+2]
        continue
        
    else:
        print("not an additive sequence")
        break
    logging.warning("loop cant be break")
if j==k[i+2]:
    print("is a additive sequence")
    logging.info("executionsucessful")
