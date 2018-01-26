import psutil

print(psutil.cpu_count())


print(psutil.cpu_count(logical=False))


print(psutil.cpu_times())


for x in range(10):
    psutil.cpu_percent(interval=1,percpu=True)