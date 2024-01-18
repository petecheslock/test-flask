from flask import Flask

app = Flask(__name__)

app.config["SECRET"] = "123123123123"

@app.route("/")
def index():
    return "please work"

@app.route("/test")
def num2():
    return "i have not lost my mind"

if __name__ == "__main__":
    app.run()