import json
from collections import OrderedDict
import pandas as pd
from pythonCode import NLP
from pythonCode import sentiment_analysis as sent

if __name__ =="__main__":
    data = pd.read_csv("../file/NLP/test_dataset.csv", encoding="UTF-8")[['Title', 'Label']]
    new_data = NLP.predict(data)
    print(new_data)
    #