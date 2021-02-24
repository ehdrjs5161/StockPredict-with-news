import pandas as pd
import requests
import time
import datetime
import re
from bs4 import BeautifulSoup

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

def day_range(begin, end):
    day_list = []
    begin = datetime.datetime.strptime(begin, "%Y.%m.%d")
    end = datetime.datetime.strptime(end, "%Y.%m.%d")

    date_gen = [begin +datetime.timedelta(days=x) for x in range(0, (end-begin).days)]
    for date in date_gen:
        day_list.append(date.strftime("%Y.%m.%d"))
    day_list.append(end.strftime("%Y.%m.%d"))
    return day_list


def parsing(name, begin, end):
    begin = datetime.datetime.strptime(begin, "%Y-%m-%d").strftime("%Y.%m.%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d").strftime("%Y.%m.%d")

    url = ("https://search.naver.com/search.naver?where=news&query={}".format(name))
    days = day_range(begin, end)
    title_result = []
    link_result = []
    date_result = []
    for day in days:
        day_url = (
            "&sm=tab_pge&sort=2&photo=0&field=1&reporter_article=&pd=3&ds={}&de={}&docid=&nso=so:da,p:from{}to{},a:all".format(
                day, day, day.replace(".", ""), day.replace(".", "")))

        page = 0
        date = datetime.datetime.strptime(day, "%Y.%m.%d").strftime("%Y-%m-%d")
        while (True):
            source_cde = requests.get(
                url + day_url + ("l&mynews=0&cluster_rank=77&start={}&refresh_start=1".format(page * 10 + 1)))
            html = BeautifulSoup(source_cde.content, "html.parser")
            news = html.select("a.news_tit")
            point = html.select("div.not_found02")
            if point:
                print(date+"'s Last Page...")
                break
            for i in news:
                date_result.append(date)
                title = i.attrs['title']
                title = re.sub('[-=+,#/\?:≑^$.@*’ \"※~&%ㆍ!	‧』\\‘|\(\)\[\]\<\>`\'…\"\“》·]', '', title)
                title_result.append(title)
                link_result.append(i.attrs['href'])
            page = page + 1
        time.sleep(0.0001)
    frame = pd.DataFrame({'Date': date_result, 'Title': title_result, 'Url': link_result})

    return frame


def crawling(name, begin, end):
    frame = parsing(name, begin, end)
    print("news crawling completed!")

    return frame

if __name__ == "__main__":
    kospi = pd.read_csv("../file/KOSPI200.csv")[['종목코드', '기업명']]
    kospi = kospi.iloc[166:]
    names = list(kospi['기업명'])
    print(names)
    for name in names:
        code = search_code(name, kospi)
        print(code)
        result = crawling(name=name, begin="2013-01-01", end="2013-12-31")
        result.to_csv("./temporary_news/" + code + "_02.csv", encoding="utf-8")
        print(code, "  ", name, "Completed!")
