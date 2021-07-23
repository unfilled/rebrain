import os
import sys
import logging
import time 

logging.basicConfig(filename='log_file.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)

i = 0
max = (int)(sys.argv[1])
wait = (int)(sys.argv[2])

for item, value in os.environ.items():
    #print (f"{item} -> {value}")
    logging.info(f"{item} -> {value}")
    i += 1
    if i >= max:
        break
    time.sleep(wait)
