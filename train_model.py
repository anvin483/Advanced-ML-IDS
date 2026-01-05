import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[["packet_length", "protocol", "src_port", "dst_port"]]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = IsolationForest(
    n_estimators=100,
    contamination=0.3,
    random_state=42
)
model.fit(X_scaled)

# Save model and scaler
joblib.dump(model, "ids_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model and scaler trained & saved")
