from flask import Flask
import pandas as pd
from pythonCode import company, method, DB_Handler
import os
import datetime
from collections import OrderedDict
mongo = DB_Handler.DBHandler()
app = Flask(__name__, static_folder='pythonCode')
app.config['JSON_AS_ASCII'] = False


@app.route('/code', methods=['GET', 'POST'])
def code():
    code_list = mongo.find


@app.route('/api', methods=['GET'])
def api():
    return {
        'userid': 1,
        'title': 'Ant: Stock Predict Application',
        'completed': False
    }

@app.route('/code/<code>', methods=['GET', 'POST'])
def predict(code):
    kospi = mongo.find_items(db_name="stockPredict", collection_name="code")
    kospi = pd.DataFrame(kospi)[['종목코드', '기업명']]
    name = method.code_to_name(kospi, code)
    comp = company.companys(name=name, code=code)
    comp.load_data()
    update = method.date_to_str(datetime.datetime.today() - datetime.timedelta(days=1))
    print(update, comp.update_day)

    if update != comp.update_day:
        comp.update_data()
        comp.model_setting(10, 28, 3)
        comp.predict_price_day1()
        comp.predict_price_day7()
        comp.result_save()

    result = mongo.find_item(condition={"code": "{}".format(comp.code)}, db_name="stockPredict", collection_name="predictResult")
    del result['_id']

    return result

@app.route('/rank', methods=['GET', 'POST'])
def rank():
    cursor = mongo.find_items(db_name="stockPredict", collection_name="rank")
    result = OrderedDict()
    result_list=[]
    for rank in cursor:
        del rank['_id']
        result_list.append(rank)
    result['result'] = result_list
    return result

if __name__ == "__main__":
    print(rank())