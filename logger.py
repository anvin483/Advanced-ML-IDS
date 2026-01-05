from datetime import datetime

def log_alert(msg):
    with open("alerts.log", "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")
