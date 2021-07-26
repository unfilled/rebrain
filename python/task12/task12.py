import psutil
import os

class PC_Memory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent = None):
        self.pc_id, self.user_name, self.memory_total, self.memory_used = pc_id, user_name, memory_total, memory_used
        if memory_percent:
            self.memory_percent = memory_percent
        else:
            self.memory_percent = round(self.memory_used/self.memory_total * 100, 1)

    def show_used_percent(self):
        print (f"PC with id {self.pc_id} used {self.memory_percent} percent of memory")

    def is_enough_memory(self):
        return (self.memory_percent < 90 and (self.memory_total - self.memory_used) / 1024 / 1024 / 1024 > 1) 

class PC_advanced(PC_Memory):
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent = None, ld_avg_1m = None, ld_avg_15m = None):
        PC_Memory.__init__(self, pc_id, user_name, memory_total, memory_used, memory_percent)
        if ld_avg_1m:
            self.ld_avg_1m = ld_avg_1m
        else:
            self.ld_avg_1m = psutil.getloadavg()[0]
        if ld_avg_15m:
            self.ld_avg_15m = ld_avg_15m
        else:
            self.ld_avg_15m = psutil.getloadavg()[2]
        
    def is_overloaded(self):
        return self.ld_avg_1m >= 3 * self.ld_avg_15m

    def __call__(self, action = 'memory'):
        if action == 'memory':
            return self.is_enough_memory()
        elif action == 'load':
            return self.is_overloaded()
        else:
            return None

    

mem = psutil.virtual_memory()
load_avg = psutil.getloadavg()

pc_a = PC_advanced(1, os.getlogin(), mem.total, mem.used, mem.percent, load_avg[0], load_avg[2])

print('is_overloaded:', pc_a.is_overloaded())
print('is_enough_memory:', pc_a.is_enough_memory())

print(pc_a())
