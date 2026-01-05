import joblib
from packet_capture import start_capture
from logger import log_alert

# Load trained model and scaler
model = joblib.load("ids_model.pkl")
scaler = joblib.load("scaler.pkl")

def detect(df):
    if df is not None:
        scaled = scaler.transform(df)
        result = model.predict(scaled)

        if result[0] == -1:
            alert = "🚨 Intrusion Detected"
            print(alert)
            log_alert(alert)
        else:
            print("✅ Normal traffic")

start_capture(detect)
