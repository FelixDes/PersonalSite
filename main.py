import json
import os
import re

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = \
    "_th{zi{qxXpNwPPWBkmdRtw}akIfadgOjtrdygLmGhb{OBawz^GIU|qpFYiZcBAhb{r]ZNr]ZzgRzqhqeZBBpo;hv_oeBnXZz{'"


@app.route("/")
def index():
    # , methods=['GET', 'POST']
    # if request.method == 'POST':
    #     if request.form.get('change') == 'eng':
    #         return render_template(
    #             "index.html", dct=get_dict_for_from_json(get_string_from_path("static/text/text.json"), "eng"))
    #     elif request.form.get('change') == 'rus':
    #         return render_template(
    #             "index.html", dct=get_dict_for_from_json(get_string_from_path("static/text/text.json"), "rus"))

    return render_template(
        "index.html", dct=get_dict_for_from_json(get_string_from_path("static/text/text.json"), "rus"))


def get_string_from_path(path):
    with open(path, "r") as file:
        return file.read()


def get_dict_for_from_json(json_string, lang):
    jsn = dict(json.loads(json_string))
    return {key: jsn[key][lang] for key in jsn.keys()}

# def link_preprocessor(dct):
#     for node in dct:
#         if node["link_preprocessor"] is not None:
#             if type(node["text"]) == list:
#                 for

if __name__ == '__main__':
    app.run(port=10000)
