import os

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = \
    "_th{zi{qxXpNwPPWBkmdRtw}akIfadgOjtrdygLmGhb{OBawz^GIU|qpFYiZcBAhb{r]ZNr]ZzgRzqhqeZBBpo;hv_oeBnXZz{'"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=10000)
