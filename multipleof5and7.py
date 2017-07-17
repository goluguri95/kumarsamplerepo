import sys
import logging
logging.basicConfig(filename='vastada.log',level=logging.DEBUG)
i=1500;
while (i>1499 and i<2701):
    if(i%7==0 and i%5==0):
        logging.debug('print the message')
        print(i)
    i=i+1
