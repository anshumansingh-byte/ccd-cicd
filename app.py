from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>CI/CD Pipeline Working!</h1><p>Flask application deployed using Jenkins and Docker.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
