from flask import Flask, render_template, request
import os
import hmac

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    valid_username = os.environ.get("DEMO_USERNAME", "")
    valid_password = os.environ.get("DEMO_PASSWORD", "")

    if (valid_username and valid_password
        and hmac.compare_digest(username, valid_username)
        and hmac.compare_digest(password, valid_password)):
        return "Login successful!"

    return "Invalid username or password", 401

if __name__ == "__main__":
    app.run(debug=False)
