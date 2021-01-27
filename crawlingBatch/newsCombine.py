import pandas as pd
import os
from pythonCode import method


def combine(code):
    news = pd.DataFrame()
    while os.path.isfile("./temporary_news/"+code+"_1.csv") and os.path.isfile("./temporary_news/"+code+"_2.csv")\
            and os.path.isfile("./temporary_news/"+code+"_3.csv") and os.path.isfile("./temporary_news/"+code+"_4.csv") and os.path.isfile("./temporary_news/"+code+"_5.csv"):
        continue
    print("news Combine completed")
    news = pd.concat([news, pd.read_csv("./temporary_news/" + code + "_1.csv")[['Date', 'Title', 'Url']]])
    news = pd.concat([news, pd.read_csv("./temporary_news/" + code + "_2.csv")[['Date', 'Title', 'Url']]])
    news = pd.concat([news, pd.read_csv("./temporary_news/" + code + "_3.csv")[['Date', 'Title', 'Url']]])
    news = pd.concat([news, pd.read_csv("./temporary_news/" + code + "_4.csv")[['Date', 'Title', 'Url']]])
    news = pd.concat([news, pd.read_csv("./temporary_news/" + code + "_5.csv")[['Date', 'Title', 'Url']]])
    news.to_csv("../news/"+code+".csv", encoding="UTF-8")

if __name__ == "__main__":
    kospi = pd.read_csv("../file/KOSPI200.csv")[['종목코드', '기업명']]
    codes = list(kospi['종목코드'])
    for code in codes:
        code = method.set_code(code)
        combine(code)
