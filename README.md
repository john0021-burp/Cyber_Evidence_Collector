# 🕵️‍♂️ Cybercrime Evidence Collector

A live forensics tool that collects browser history and system information across Chrome, Edge, Brave, Firefox, and Safari (on macOS). Generates structured JSON output and an HTML report for investigators.

---

## 🚀 Features

- ✅ Collects browser history from:
  - Google Chrome
  - Microsoft Edge
  - Brave Browser
  - Mozilla Firefox
  - Safari (macOS only)
- ✅ Generates:
  - `browser_history.json` (raw evidence)
  - `report.html` (forensic summary)
- ✅ Works via:
  - CLI (`collector.py`)
  - GUI (`gui.py`)
- ✅ Fully cross-platform: Windows and macOS (limited Linux support)
- ✅ Can be packaged as `.exe` for offline forensic use

---

## 📁 Folder Structure

cyber_evidence_collector/
│
├── collector.py # Main CLI script
├── gui.py # GUI version
├── utils/
│ ├── browser_history.py # Handles all browser history collection
│ └── system_info.py # (Optional) for system metadata
├── templates/
│ └── report_template.html # HTML template for reports
├── output/
│ └── [timestamped folders] # Where reports are saved
├── requirements.txt # Python dependencies
└── README.md 

# This file


---

## 🛠️ Installation

### 🔹 Option 1: Run as Python script

1. Install Python 3.8+
2. Install required packages:

```bash
pip install -r requirements.txt
''''


##Run the tool

python collector.py     # CLI version
python gui.py           # GUI version
