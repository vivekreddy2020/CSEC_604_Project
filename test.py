
import time
timeout = int(5)
timeout = timeout+ int(time.ctime()[17:19])

print(timeout)
while(True):
    
    if(timeout == int(time.ctime()[17:19])):
        print("done")
        break


