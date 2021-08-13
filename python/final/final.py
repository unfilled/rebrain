import logging, time, Client

logging.basicConfig(filename='log.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)

#log start here
logging.info("Started")
c = Client.Client()

while True:
    info = c.collect_system_info()
    c.make_post('http://127.0.0.1:8000/api/servers/add', info)
    time.sleep(60)
