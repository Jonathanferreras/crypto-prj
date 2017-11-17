import client
import server
import os
import time
import sys

sys.dont_write_bytecode = True

if __name__ == '__main__':
    os.system('python server.py &')
    time.sleep(2)
    os.system('python client.py')
