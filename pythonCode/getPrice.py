from pandas_datareader import data
import pandas as pd
import os
from pykrx import stock
import datetime
from pythonCode import method


def stock_price(code, begin):
    code = method.set_code(code)
    code = code+'.KS'
    frame = data.get_data_yahoo(code, begin)
    frame.to_csv("./price/"+code+".csv", encoding="UTF-8")

    return frame

def market_info (code, begin):
    today = datetime.datetime.today().strftime("%Y%m%d")
    market = pd.DataFrame()
    code = method.set_code(code)
    print(code)
    if os.path.isfile("./market_info/" + code + ".csv"):
        market = pd.read_csv("./market_info/" + code + ".csv", encoding="UTF-8")
        last_day = datetime.datetime.strptime(market.iloc[-1]['날짜'], "%Y-%m-%d")
        last_day = datetime.datetime.strftime(last_day, "%Y%m%d")
        print(last_day, today, code)
        print(type(last_day), type(today), type(code))
        temp = stock.get_market_fundamental_by_date(last_day, today, code)
        market = pd.concat([market, temp])
    else:
        date = begin.replace("-", "")
        print(date, today, code)
        print(type(date), type(today), type(code))
        temp = stock.get_market_fundamental_by_date(date, today, code)
        market = pd.concat([market, temp])

    return market


# if __name__ =="__main__":
#     kospi200 = pd.read_csv("./file/KOSPI200.csv", encoding="UTF-8")[['종목코드', '기업명']]
#     name = "셀트리온"
#     code = method.search_code(name, kospi200)
#     for code, name in zip(kospi200['종목코드'], kospi200['기업명']):
#         price = stock_price(code, begin="2012-01-01")
#         price.to_csv("./price/"+method.set_code(code)+".csv", encoding="cp949")