import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print u"\u001b[0m"
import time, sys
def loading():
    print "Loading..."
    for i in range(0, 100):
        time.sleep(0.01)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print
    
loading()