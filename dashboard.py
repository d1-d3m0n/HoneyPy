from flask import Flask, render_template
import os

app = Flask(__name__)

LOG_DIR = "logs"

def parse_log(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        lines = f.readlines()

    entries = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            timestamp = line.split("]")[0].strip("[").strip()
            service = line.split("]")[1].strip("[").strip()
            message = "]".join(line.split("]")[2:]).strip()
            entries.append({
                "timestamp": timestamp,
                "service": service,
                "message": message
            })
        except Exception:
            continue
    return entries

@app.route("/")
def index():
    ssh_logs = parse_log(os.path.join(LOG_DIR, "ssh_activity.log"))
    http_logs = parse_log(os.path.join(LOG_DIR, "http_activity.log"))
    return render_template("dashboard.html", ssh_logs=ssh_logs, http_logs=http_logs)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
