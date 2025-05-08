# === utils/recent_files.py ===
import os
import glob
import time

def collect_recent_files():
    user_profile = os.environ.get("USERPROFILE")
    recent_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Recent')
    files = []
    if not os.path.exists(recent_path):
        return {"error": "Recent files not found"}

    for file in glob.glob(os.path.join(recent_path, '*.lnk')):
        try:
            access_time = time.ctime(os.path.getatime(file))
            files.append({"file": os.path.basename(file), "last_accessed": access_time})
        except Exception:
            continue
    return files