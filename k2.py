#!/usr/bin/pyhton2

import psutil
c=psutil.virtual_memory()
a=psutil.cpu_times()
b=psutil.swap_memory()
for x in range(3):
    psutil.cpu_times_percent(interval=1, percpu=False)
print a
print b
print c
