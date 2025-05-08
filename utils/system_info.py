# === utils/system_info.py ===
import platform
import socket
import getpass

def collect_system_info():
    return {
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor()
    }