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

mem = psutil.virtual_memory()
pc_a = PC_Memory(1, os.getlogin(), mem.total, mem.used, mem.percent)
pc_b = PC_Memory(2, os.getlogin(), mem.total, mem.used)


pc_a.show_used_percent()
pc_b.show_used_percent()

print (pc_a.is_enough_memory())
print (pc_b.is_enough_memory())