import pandas as pd
import datetime
import os
from pythonCode import getPrice, getNews, method

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

def load_data(company):
    code = set_code(company.code)
    try:
        if not os.path.isfile("../price/"+code+".csv"):
            price = getPrice.stock_price(code, "2012-01-01")
            price.to_csv("../price/"+code+'.csv', encoding="UTF-8")
        if not os.path.isfile("../news/"+code+".csv"):
            today = method.date_to_str(datetime.datetime.today())
            news = getNews(company.name, begin="2012-01-01", end=today)
        news = pd.read_csv("../news/"+code+".csv", encoding="utf-8")[['Date', 'Title', 'Url']]
        price = pd.read_csv("../price/"+code+".csv", encoding="utf-8")[['Date', 'High', 'Low', 'Open', 'Close', 'Volume']]

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

def day_range(begin, end):
    day_list = []
    begin = datetime.datetime.strptime(begin, "%m.%d")
    end = datetime.datetime.strptime(end, "%m.%d")

    date_gen = [begin +datetime.timedelta(days=x) for x in range(0, (end-begin).days)]
    for date in date_gen:
        day_list.append(date.strftime("%m.%d"))
    day_list.append(end.strftime("%m.%d"))
    return day_list

def news_union(code):
    news = pd.DataFrame()
    for i in range(1, 6):
        temp = pd.read_csv("./crawlingBatch/temporary_news/"+code+"_"+str(i)+".csv")[['Date', "Title", 'Url']]
        news = pd.concat([news, temp])

    return news

def merge(news, price, col1, col2):
    data = pd.merge(price, news, left_on="{}".format(col1), right_on="{}".format(col2))
    data.drop([col2], axis='columns', inplace=True)
    return data

def re_sizing(batch_size, data):
    batch = batch_size
    size = len(data)
    cnt = 0
    if size % batch != 0:
        while size % batch != 0:
            size = size - 1
            cnt += 1
    return cnt

def inverseTransform(Scaler, normed_data):
    real_data = []
    for i in range(0, len(normed_data)):
        temp = []
        for j in range(0, len(normed_data[0])):
            temp.append(Scaler.inverse_transform([[normed_data[i][j], 0]])[0][0])
        real_data.append(temp)
    return real_data

def inverseTransform_day7(Scaler, normed_data):
    real_data = []
    for i in range(0, len(normed_data)):
        temp = []
        for j in range(0, len(normed_data[0])):
            temp.append(Scaler.inverse_transform([[normed_data[i][j], 0]])[0][0])
        real_data.append(temp)

    return real_data
