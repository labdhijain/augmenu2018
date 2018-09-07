#!/usr/bin/pyhton2

import psutil
psutil.virtual_memory()
psutil.cpu_times()
psutil.swap_memory()
for x in range(3):
    psutil.cpu_times_percent(interval=1, percpu=False)

