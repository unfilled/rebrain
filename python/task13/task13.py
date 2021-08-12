import psutil
import os

class PercentError(Exception):
    pass

class PC_Memory:
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent = None):
        self.pc_id, self.user_name = pc_id, user_name
        #memory_total, memory_used checks
        try:
            self.memory_total = int(memory_total)
            self.memory_used = int(memory_used)
            if self.memory_total <= 0 or self.memory_used > self.memory_total or self.memory_used < 0:
                raise ValueError
        except ValueError:
            print('wrong memory value, default value used')
            self.memory_total = 100 * 1024 * 1024 * 1024 #default 100GiB
            self.memory_used = 0                         #default 0 

        #memory_percent checks
        if memory_percent:
            try:
                self.memory_percent = float(memory_percent)
            except ValueError:
                print('wrong percent value, value calculated automatically')
                self.memory_percent = round(self.memory_used/self.memory_total * 100, 1)
            else:
                if memory_percent < 0 or memory_percent > 100:
                    raise PercentError
        else:
            self.memory_percent = round(self.memory_used/self.memory_total * 100, 1)

    def show_used_percent(self):
        print (f"PC with id {self.pc_id} used {self.memory_percent} percent of memory")

    def is_enough_memory(self):
        return (self.memory_percent < 90 and (self.memory_total - self.memory_used) / 1024 / 1024 / 1024 > 1) 

mem = psutil.virtual_memory()
# #ok
# pc_a = PC_Memory(1, os.getlogin(), mem.total, mem.used, mem.percent)
# print(pc_a.memory_total, pc_a.memory_used, pc_a.memory_percent)

# #incorrect mem.used
# pc_b = PC_Memory(1, os.getlogin(), mem.total, mem.used*10000, mem.percent)
# #wrong memory value, default value used

# #incorrect mem.total
# pc_c = PC_Memory(1, os.getlogin(), -1, mem.used, mem.percent)
# #wrong memory value, default value used

# #incorrect mem.total
# pc_d = PC_Memory(1, os.getlogin(), 'a', mem.used, 'b')
# #wrong memory value, default value used
# #wrong percent value, value calculated automatically

# #incorrect memory percent
# #pc_e = PC_Memory(1, os.getlogin(), mem.total, mem.used, -1)
# #__main__.PercentError


#incorrect memory percent
pc_e = PC_Memory(1, os.getlogin(), 0, 10, 'a')
print (pc_e.memory_percent, pc_e.memory_total, pc_e.memory_used)
#__main__.PercentError
