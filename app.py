from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("alerts.log") as f:
            return "<br>".join(f.readlines())
    except:
        return "No alerts yet"

app.run(debug=True)
