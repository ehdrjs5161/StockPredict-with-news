import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler 
import datetime

def set_code(code):
    code = str(code)
    if len(code) < 6:
        for j in range(0, 6 - len(code)):
            code = '0' + code
    return code

def search_code(company, frame):
    codes = []
    name = company
    code = frame['기업명'] == name
    code = list(frame['종목코드'][code])
    codes.append(code[0])
    code = set_code(str(codes[0]))

    return code

def load_data(code):
    code = set_code(code)
    try:
        news = pd.read_csv("./news/"+code+".csv", encoding="cp949")[['Date', 'Title', 'Url']]
        price = pd.read_csv("./price/"+code+".csv", encoding="cp949")[['Date', 'High', 'Low', 'Open', 'Close', 'Volume']]
        return news, price

    except FileNotFoundError as e:
        print(e)
        return pd.DataFrame(), pd.DataFrame()

def swift_type(news):
    days = []
    for i in range(0, len(news)):
        day = datetime.datetime.strptime(news[i], "%Y.%m.%d").strftime("%Y-%m-%d")
        days.append(day)
    news['date'] = days

    return news

def str_to_date(string):
    date = datetime.datetime.strptime(string, "%Y-%m-%d")
    return date

def date_to_str(date):
    date = date.strftime("%Y-%m-%d")
    return date


