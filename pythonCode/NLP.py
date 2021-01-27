from konlpy.tag import Okt
import pandas as pd
if __name__ =="__main__":
    stopwords = [',', '…', '-', '\'', '·', '‘', '\"', '!', '`', '…', '’', '의', '가', '이', '은',
                 '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']

    okt = Okt()
    result = []
    sentence = "롯데마트는여기서5분거리입니다."
    temp = okt.morphs(sentence, stem=True)
    temp = [word for word in temp if not word in stopwords]
    result.append(temp)

    print(result)