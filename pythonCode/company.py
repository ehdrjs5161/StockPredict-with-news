import pandas as pd
import datetime
from pythonCode import modeling, method, getNews, getPrice, NLP
from pythonCode import sentiment_analysis as sent
import os
import json
from collections import OrderedDict

class companys:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.news =None
        self.price = None
        self.label = None
        self.newNews = None
        self.newPrice = None
        self.features = None
        self.model_day1 = None
        self.model_day7 = None
        self.result_day1 = None
        self.result_day7 = None
        self.update_day = None

    def load_data(self):
        self.news, self.price = method.load_data(self)
        self.update_day = self.news['Date'].iloc[-1]
        self.news = sent.labeling(self)
        # self.news = NLP.predict(self.news)
        self.news.to_csv("news/processed_news/"+str(self.code)+".csv", encoding="UTF-8")
        print(self.update_day)

    def update_data(self):
        yesterday = method.date_to_str(datetime.datetime.today()-datetime.timedelta(days=1))
        last_news = self.news['Date'].iloc[-1]
        last_news = method.str_to_date(last_news)
        self.update_day = last_news

        yesterday = method.str_to_date(yesterday)
        # 가지고 있는 뉴스 데이터의 마지막 날짜와 어제 날짜를 비교하여 뉴스 데이터 중 어제 뉴스가 포함되지 않다면 크롤링해서 저장.
        if self.update_day < yesterday:
            print("Update News & Price")
            begin = self.update_day + datetime.timedelta(days=1)
            self.newNews = getNews.crawling(name=self.name, begin=method.date_to_str(begin), end=method.date_to_str(yesterday))
            print(self.newNews)
            self.news = pd.concat([self.news, self.newNews])
            self.news.reset_index(drop=True, inplace=True)
            self.news.to_csv("news/"+self.code+".csv", encoding="UTF-8")

            self.price = getPrice.stock_price(self.code, begin="2012-01-01")
            temp = getPrice.stock_price(self.code, begin=self.update_day)
            temp.to_csv("price/"+self.code+".csv", encoding="UTF-8")
            self.newPrice = pd.read_csv("price/"+self.code+".csv", encoding="UTF-8")[['Date', 'High', 'Low', 'Open', 'Close', 'Volume']]
            self.price.to_csv("price/"+self.code+".csv", encoding="UTF-8")
            self.price = pd.read_csv("price/"+self.code+".csv", encoding="UTF-8")

            print("Updating News & Price is completed!")
        else:
            print(self.name+"'s News & Price data are already Updated!")
        self.update_day = yesterday

    def model_setting(self, batch, term, features):
        self.features = features
        if not os.path.isfile("model/"+self.code+"/saved_model.pb"):
            print("predict 1 day Model Compiling...")
            self.model_day1 = modeling.modeling(batch, term, self.features)
            self.model_day1 = modeling.model_educate(self, term, batch, 1)

        else:
            self.model_day1 = modeling.load_model(self.code, predict_day=1)

        if not os.path.isfile("model_day7/"+self.code+"/saved_model.pb"):
            print("predict 7 days Model Compiling...")
            self.model_day7 = modeling.modeling_day7(batch, term, self.features)
            self.model_day7 = modeling.model_educate(self, term, batch, 7)

        else:
            self.model_day7 = modeling.load_model(self.code, predict_day=7)

    def predict_price_day1(self):
        self.result_day1 = modeling.predict_day1(self)

    def predict_price_day7(self):
        self.result_day7 = modeling.predict_day7(self)

    def model_update(self):
        # 한번 모델링 해놓으면 당분간 안해도 됨.
        self.model_day1, self.model_day7 = modeling.update_model(self)
        print("Model Update Completed!")

    def result_save(self):
        file_path = "./json_result/" + self.code
        result = OrderedDict()
        price_temp = OrderedDict()
        result["code"] = self.code
        result["name"] = self.name
        temp = []
        for i in range(0, len(self.result_day1['Time'])):
            price = {'Date': '{}'.format(self.result_day1['Time'][i]),
                     'Price': '{}'.format(int(self.result_day1['Price'][i]))}
            temp.append(price)
        price_temp['day1'] = temp

        temp = []
        for i in range(0, len(self.result_day7['Time'])):
            price = {'Date': '{}'.format(self.result_day7['Time'][i]),
                     'Price': '{}'.format(int(self.result_day7['Price'][i]))}
            temp.append(price)
        price_temp['day7'] = temp
        result['price'] = price_temp

        temp = []
        for i in range(0, len(self.result_day7['Predict'][0])):
            predict = {'Date': '{}'.format(str(i + 1) + " day After"),
                       'Price': '{}'.format(int(self.result_day7["Predict"][0][i]))}
            temp.append(predict)
        result['predict'] = {'day1': '{}'.format(int(self.result_day1['Predict'][0][0])), 'day7': temp}
        result = json.dumps(result, ensure_ascii=False, indent="\t")
        with open(file_path, "w") as outfile:
            json.dump(result, outfile, indent="\t")

        rate_result = OrderedDict()
        rate_result['code'] = self.code
        rate_result['name'] = self.code

