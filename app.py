from flask import Flask, jsonify
import pandas as pd
import json
from collections import OrderedDict
from pythonCode import company, method
import os
app = Flask(__name__, static_folder='pythonCode')
app.config['JSON_AS_ASCII'] = False

@app.route('/api', methods=['GET'])
def api():
    return {
        'userid': 1,
        'title': 'Ant: Stock Predict Application',
        'completed': False
    }

@app.route('/code/<code>', methods=['GET', 'POST'])
def predict(code):
    file_path = "./json_result/withNews/" + code + ".json"
    # if not os.path.isfile(./json_result/"+code):
    if not os.path.isfile("./json_result/withNews/"+code+".json"):
        kospi = pd.read_csv("file/KOSPI200.csv")[['종목코드', '기업명']]
        name = method.code_to_name(kospi, code)
        comp = company.companys(name=name, code=code)
        comp.load_data()
        # comp.update_data()
        comp.model_setting(10, 28, 3)
        # comp.predict_price_day1()
        # comp.predict_price_day7()
        # comp.result_save()

    with open(file_path, "r") as json_file:
        result = json.load(json_file)
    return result["{}".format(code)]

@app.route('/rank', methods=['GET', 'POST'])
def rank():
    file_path = "json_result/withNews/Rank.json"
    if os.path.isfile(file_path):
        with open(file_path, "r") as json_file:
            result = json.load(json_file)

        return result


if __name__ == "__main__":
    result = predict("068270")
    # result = rank()
    # print(result)