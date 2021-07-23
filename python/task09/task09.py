import os
import psutil

def get_info():
    mem = psutil.virtual_memory()
    return {
        'user_name': os.getlogin(),
        'memory_total': mem.total,
        'memory_used': mem.used,
        'memory_percent': mem.percent
    }
    