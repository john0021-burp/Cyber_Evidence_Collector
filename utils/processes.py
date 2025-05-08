# === utils/processes.py ===
import psutil
from datetime import datetime

def collect_processes():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'create_time']):
        try:
            proc_info = proc.info
            proc_info['create_time'] = datetime.fromtimestamp(
                proc_info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
            process_list.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return process_list