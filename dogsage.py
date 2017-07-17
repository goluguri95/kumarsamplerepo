import logging
import datetime
import sys

logging.basicConfig(filename='kumar.log',Level=logging.DEBUG)

i=int(sys.argv[1])
logging.DEBUG('thismessage ')
if (i<=2):
    k=k*10.5
    logging.DEBUG('thismessage ')
    print('The dogs age in dogs years is'+ str( k))
else:
    k=2*10.5+(i-2)*4
    print('The dogs age in dogs years is'+ str( k))
    
