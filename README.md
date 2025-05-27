# 🛡️ Honeypy – SSH & HTTP Honeypot with Live Dashboard

Honeypy is a lightweight, customizable honeypot system designed to mimic vulnerable **SSH** and **HTTP login services**, capture attack attempts, and display them in a live **web-based dashboard**.

Built for learning, monitoring, and basic threat intelligence collection, it's ideal for cybersecurity students, CTF organizers, researchers, and hobbyists.

---

## 📸 Preview

![Dashboard Preview](dashboard.png)  
_Real-time attack logs displayed in the web dashboard_

---

## 🚀 Features

✅ **SSH Honeypot** — Logs IPs, usernames, passwords used in brute-force attempts  
✅ **HTTP Honeypot** — Fake login page capturing credentials  
✅ **Live Web Dashboard** — Flask-based dashboard for real-time monitoring  
✅ **Threaded Execution** — Run dashboard and honeypots simultaneously  
✅ **Simple Logging** — All events saved to organized `.log` files  
✅ **Command-line Config** — Easily configure address, ports, and credentials

---

## 🧪 How It Works

Honeypy simulates vulnerable endpoints:
- **SSH Honeypot** uses Paramiko to fake a shell and log credentials.
- **HTTP Honeypot** runs a fake login form and logs POST attempts.
- **Dashboard** uses Flask to read logs and show events in a web UI.

All logs are stored in the `logs/` directory and displayed live in the dashboard.

---

## 🛠️ Requirements

- Python 3.8+
- Flask
- Paramiko

Install them:

```bash
pip install -r requirements.txt

## 📥 Installation

Follow these steps to get started:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/honeypy.git
cd honeypy

2️⃣ Install Dependencies

Make sure Python 3.8+ is installed.

pip install -r requirements.txt

3️⃣ Give Execution Permissions (if on Linux/macOS)

chmod +x honeypy.py
chmod +x dashboard.py

🚀 Quick Start
▶️ Run SSH Honeypot with Dashboard

python3 honeypy.py -a 0.0.0.0 -p 2222 --ssh --dashboard

▶️ Run HTTP Honeypot with Dashboard

python3 honeypy.py -a 0.0.0.0 -p 8080 --http --dashboard -u admin -pw password

    📌 You can customize the username and password for the HTTP honeypot login form using -u and -pw.

🔎 Running the Dashboard Separately

You can also launch the dashboard alone (useful for reviewing logs later):

python3 dashboard.py

Then visit: http://localhost:5000

