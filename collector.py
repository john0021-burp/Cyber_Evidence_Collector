# === collector.py ===
import os
import json
from datetime import datetime
from utils.system_info import collect_system_info
from utils.processes import collect_processes
from utils.network import collect_network_connections
from utils.browser_history import collect_all_browser_histories
from utils.clipboard import collect_clipboard
from utils.recent_files import collect_recent_files
from utils.report_generator import generate_html_report

def create_output_dir():
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    output_dir = os.path.join("output", timestamp)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    output_dir = create_output_dir()

    save_to_file(collect_system_info(), os.path.join(output_dir, "system_info.json"))
    save_to_file(collect_processes(), os.path.join(output_dir, "processes.json"))
    save_to_file(collect_network_connections(), os.path.join(output_dir, "network_connections.json"))
    save_to_file(collect_all_browser_histories(), os.path.join(output_dir, "browser_history.json"))
    save_to_file(collect_clipboard(), os.path.join(output_dir, "clipboard.json"))
    save_to_file(collect_recent_files(), os.path.join(output_dir, "recent_files.json"))

    html_path = generate_html_report(output_dir)
    print(f"[+] Data collected. HTML report generated at: {html_path}")

if __name__ == "__main__":
    main()