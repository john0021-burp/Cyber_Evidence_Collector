# === utils/report_generator.py ===
import os
import json

def generate_html_report(output_dir):
    html_path = os.path.join(output_dir, "report.html")
    html = "<html><head><title>Cybercrime Evidence Report</title></head><body>"
    html += "<h1>Cybercrime Evidence Report</h1>"

    for file in sorted(os.listdir(output_dir)):
        if file.endswith(".json"):
            html += f"<h2>{file}</h2><pre>"
            with open(os.path.join(output_dir, file), 'r') as f:
                html += json.dumps(json.load(f), indent=4)
            html += "</pre><hr>"

    html += "</body></html>"
    with open(html_path, 'w') as f:
        f.write(html)

    return html_path