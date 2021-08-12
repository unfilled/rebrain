import requests, platform, os, psutil, logging
class Client:
    def __init__(self, ip_address = None, name = None, description = None, server = None):
        # ip
        if ip_address:
            self.ip_address = ip_address
        else:
            try:
                self.ip_address = requests.get('https://api.my-ip.io/ip').text
            except:
                self.ip_address = '127.0.0.1'

        # hostname
        if name:
            self.name = name
        else:
            self.name = platform.uname().node

        # description
        if description:
            self.description = description
        else:
            if os.environ.get('DESC'):
                self.description = os.environ.get('DESC')
            else:
                self.description = 'None'

        # register client on a given server
        if server:
            self.server = server            
        else:
            self.server = 'http://127.0.0.1:8000/api/servers/add'
        self.register(self.server)

    # make http-post
    def make_post(self, url, data):
        try:
            r = requests.post(url, data)
            if r.status_code >= 200 and r.status_code < 300:    
                #success don't have to log
                pass
            else:
                #log error
                logging.error(f"bad status code: {r.status_code}")
        except:
            # some logging here
            logging.error("execption whlie making post request")

    def register(self, url):
        data = {}
        data['ip_address'] = self.ip_address
        data['name'] = self.name
        data['description'] = self.description
        try:
            self.make_post (url, data)
            logging.info("server registered")
        except:
            logging.error("error registering client")

    def collect_system_info(self):
        info = {}
        info['host_information'] = {'sysname': platform.uname().system, 'hostname': platform.uname().node}
        
        # network {'interface': up/down, 'mtu': ... }
        net = psutil.net_if_stats()
        d = []

        for i in net:
            if net[i]:
                status = 'up'
            else:
                status = 'down'
            d.append({i: status, 'mtu': net[i].mtu, 'duplex': net[i].duplex, 'speed': net[i].speed})
        info['network'] = d

        # disk {'disk: ..., 'mountpoint': ..., 'file_system_type', 'total': ..., 'used': ....}   
        disk = psutil.disk_partitions()
        d = []
        for device in disk:
            d.append({'disk': device.device, 'mountpoint': device.mountpoint, 'file_system_type': device.fstype, 
            'total': psutil.disk_usage(device.mountpoint).total, 'used': psutil.disk_usage(device.mountpoint).used})   
        info['disk'] = d

        # memory 'memory': {'memory_total': ..., 'memory_used': ..., 'memory_percent': ...}, 
        mem = psutil.virtual_memory()
        info['memory'] = {'memory_total': mem.total, 'memory_used': mem.used, 'memory_percent': mem.percent}

        #cpu 'cpu': {'cpu_cores': ..., 'cpu_physical_cores': ..., 'cpu_freqency': {...}}, 
        freq = psutil.cpu_freq()
        info['cpu'] = {'cpu_cores': psutil.cpu_count(), 'cpu_physical_cores': psutil.cpu_count(logical = False),
        'cpu_frquency': {'current': freq.current, 'min': freq.min, 'max': freq.max}}

        # la 'load_average': {'1 min': ..., '5 min': ..., '15 min': ...}}}
        la = psutil.getloadavg()
        info['load_average'] = {'1 min': la[0], '5 min': la[1], '15 min': la[2]}
        
        #log collected data
        logging.info(f"collected data: {info}")

        return info