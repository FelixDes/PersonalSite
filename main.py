import json
import os
import re

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = \
    "_th{zi{qxXpNwPPWBkmdRtw}akIfadgOjtrdygLmGhb{OBawz^GIU|qpFYiZcBAhb{r]ZNr]ZzgRzqhqeZBBpo;hv_oeBnXZz{'"


@app.route("/")
def index():
    return render_template(
        "index.html", dct=get_dict_for_from_json(get_string_from_path("static/text/text.json"), "rus"))


# def build_html_for_json(html_path, json_path, lang) -> str:
#     regex = r'\|\|\w+\|\|'
#
#     dct = json.loads(get_string_from_path(json_path))
#     html = get_string_from_path(html_path)
#     match = re.search(regex, html)
#     while match is not None:
#         key = html[match.start(): match.end()]
#         html =
#           html.replace(key, str(dct[key.replace("||", "").replace("||", "")][lang]["data"].replace("\n", "<br>")))
#         match = re.search(regex, html)
#     return html


def get_string_from_path(path):
    with open(path, "r") as file:
        return file.read()


def get_dict_for_from_json(json_string, lang):
    jsn = dict(json.loads(json_string))
    return {key: jsn[key][lang] for key in jsn.keys()}


if __name__ == '__main__':
    app.run(port=10000)
