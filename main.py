import psutil
import time

def monitor_cpu_usage(threshold_percent):
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)

        print(f"Total CPU Usage: {cpu_percent}%")

        if cpu_percent > threshold_percent:
            processes = psutil.process_iter(attrs=['pid', 'name', 'cpu_percent'])
            for process in processes:
                try:
                    process_info = process.info
                    if process_info['cpu_percent'] > threshold_percent:
                        print(f"Process ID: {process_info['pid']}, Name: {process_info['name']}, CPU Usage: {process_info['cpu_percent']}%")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        time.sleep(1)

if __name__ == "__main__":
    threshold = 50.0
    monitor_cpu_usage(threshold)
