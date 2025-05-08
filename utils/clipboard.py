# === utils/clipboard.py ===
import pyperclip

def collect_clipboard():
    try:
        return {"clipboard": pyperclip.paste()}
    except Exception as e:
        return {"error": str(e)}