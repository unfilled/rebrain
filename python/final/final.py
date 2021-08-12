import logging, time, Client

logging.basicConfig(filename='log.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)

#log start here
logging.info("Started")
c = Client.Client()

while True:
    info = c.collect_system_info()
    c.make_post('some url', info)
    time.sleep(60)
