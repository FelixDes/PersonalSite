import json
import os
import re

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = \
    "_th{zi{qxXpNwPPWBkmdRtw}akIfadgOjtrdygLmGhb{OBawz^GIU|qpFYiZcBAhb{r]ZNr]ZzgRzqhqeZBBpo;hv_oeBnXZz{'"


@app.route("/")
def index():
    return render_template("index.html", content=build_html_for_json("static/raw_templates/index.html", "static/text"
                                                                                                        "/text.json",
                                                                     "rus"))


def build_html_for_json(html_path, json_path, lang) -> str:
    dct = json.loads(get_string_from_path(json_path))
    html = get_string_from_path(html_path)
    match = re.search(r'{{\w+}}', html)
    while match is not None:
        key = html[match.start(): match.end()]
        html = html.replace(key, dct[key.replace("{{", "").replace("}}", "")][lang]["text"].replace("\n", "<br>"))
        match = re.search(r'{{\w+}}', html)
    return html


def get_string_from_path(path):
    with open(path, "r") as file:
        return file.read()


if __name__ == '__main__':
    app.run(port=10000)
