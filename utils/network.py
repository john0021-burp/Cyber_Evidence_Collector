# === utils/network.py ===
import psutil

def collect_network_connections():
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        try:
            info = {
                "fd": conn.fd,
                "family": str(conn.family),
                "type": str(conn.type),
                "laddr": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "",
                "raddr": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "",
                "status": conn.status,
                "pid": conn.pid,
                "process_name": psutil.Process(conn.pid).name() if conn.pid else None
            }
            connections.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return connections