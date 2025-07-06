from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Railway!</h1><p>This is a simple Flask app.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway needs this
    app.run(host="0.0.0.0", port=port)
