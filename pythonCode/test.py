import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
from pykrx import stock
import datetime
from pythonCode import method
import os
from statsmodels.stats.outliers_influence import variance_inflation_factor

def market_info (code, start_date):
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
        date = start_date.replace("-", "")
        print(date, today, code)
        print(type(date), type(today), type(code))
        temp = stock.get_market_fundamental_by_date(date, today, code)
        market = pd.concat([market, temp])

    return market
data = pd.read_csv("../price/068270.csv", encoding="UTF-8")[['Date', 'Close', 'Open', 'High', 'Low', 'Volume']]
data2 = data
market = stock.get_market_fundamental_by_date("20120101", "20201231", "068270")
print(market)
# vif1 = pd.DataFrame()
data2.pop('Date')
# print(data2.corr())
# cmap = sns.light_palette("green", as_cmap=True)
# sns.heatmap(data.corr(), annot=True, cmap=cmap)
# plt.show()
#
# vif1['VIF'] = [variance_inflation_factor(data.values, i) for i in range(data2.shape[1])]
# vif1['Features'] = data.columns
# print(vif1)

data.pop('Open')
data.pop('High')
data.pop('Low')
vif = pd.DataFrame()
print(data.corr())
cmap = sns.light_palette("green", as_cmap=True)
sns.heatmap(data.corr(), annot=True, cmap=cmap)
# plt.show()
vif['VIF'] = [variance_inflation_factor(data.values, i) for i in range(data.shape[1])]
vif['Features'] = data.columns
print(vif)
#
