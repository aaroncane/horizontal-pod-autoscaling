from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    lst = [random.randint(0, 10**6) for _ in range(10**6)]
    lst.sort()

    return "ok"



if __name__ == "__main__":
    app.run(debug=True)
