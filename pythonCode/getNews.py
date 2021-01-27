import pandas as pd
import requests
import time
import datetime
from bs4 import BeautifulSoup

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
                title_result.append(i.attrs['title'])
                link_result.append(i.attrs['href'])
            page = page + 1
        time.sleep(0.0001)

    frame = pd.DataFrame({'Date': date_result, 'Title': title_result, 'Url': link_result})

    return frame


def crawling(name, begin, end):
    frame = parsing(name, begin, end)
    print("news crawling completed!")

    return frame

    # else:
    #     frame = pd.read_csv("./newsdata/"+code+".csv", encoding="UTF-8")[['date', 'title', 'url']]
    #     print("loading previous news data")
    #     last_date = frame['date'].iloc[-1]
    #     first_date = frame['date'].iloc[0]
    #     # 뉴스데이터의 날짜를 저장한 변수,
    #
    #     # first = 가지고 있는 뉴스데이터 중 가장 오래된 뉴스의 날짜
    #     # last = 가지고 있는 뉴스데이터 중 가장 최신 뉴스의 날짜
    #
    #     # begin, end 크롤링을 요청한 뉴스데이터 기간
    #     first = datetime.datetime.strptime(str(first_date), "%Y.%m.%d")
    #     last = datetime.datetime.strptime(str(last_date), "%Y.%m.%d")
    #     # first = first_date
    #     # last = last_date
    #
    #     # print(begin, end, first, last)
    #     begin_t = datetime.datetime.strptime(begin, "%Y.%m.%d")
    #     end_t = datetime.datetime.strptime(end, "%Y.%m.%d")
    #
    #     # print(begin_t, end_t, first, last)
    #     # print(type(begin_t), type(end_t), type(first), type(last))
    #     # 크롤링하고자 하는 뉴스가 현재 갖고 있는 뉴스데이터 보다 오래된 것일 경우
    #     if begin_t < end_t < first:
    #         first_date = datetime.datetime.strftime(first - datetime.timedelta(days=1), "%Y.%m.%d")
    #         temp_frame = parsing(code, begin, first_date)
    #         temp_frame = pd.concat([frame, temp_frame])
    #         # temp_frame.to_csv("./newsdata/"+code+".csv")
    #         return temp_frame
    #     elif last < end_t:
    #         print(begin, end)
    #         temp_frame = parsing(code, begin, end)
    #         temp_frame = pd.concat([frame, temp_frame])
    #         # temp_frame.to_csv("./newsdata/"+code+".csv", encoding="UTF-8")
    #         return temp_frame
    #
    #     else:
    #         print(last, end_t)
    #         print("현재 가지고 있는 뉴스파일의 이전기간, 혹은 이후 기간만 가능 날짜다시 학인.")
    #
    # return frame
