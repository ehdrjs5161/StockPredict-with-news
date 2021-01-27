import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
from pythonCode import method
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
font_loc = '../file/Hancom Gothic Regular.ttf'
font_name=fm.FontProperties(fname=font_loc).get_name()
plt.rc('font', family=font_name)

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    tf.config.experimental.set_memory_growth(gpus[0], True)
  except RuntimeError as e:
    print(e)

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

def create_dataset(data, term, predict_days):
    x_list, y_list = [], []
    for i in range(len(data) - (term + predict_days)+1):
        x_list.append(data[i:(i+term), 0:])
        y_list.append(data[i+term:(i+term+predict_days), 0])
    x_ary = np.array(x_list)
    y_ary = np.array(y_list)
    x_ary = np.reshape(x_ary, (x_ary.shape[0], x_ary.shape[1], x_ary.shape[2]))

    return x_ary, y_ary

def load_model(code, predict_day):
    try:
        if predict_day == 1:
            model = keras.models.load_model("../model/"+code)
        elif predict_day == 7:
            model = keras.models.load_model("../model_day7/"+code)
        else:
            print("Deep Learning Model Not Found Error")
        return model

    except FileNotFoundError as e:
        print(e)
        print("Deep Learning Model Not Found Error")

def modeling(batch, term, features):
    model = keras.Sequential()
    model.add(keras.layers.LSTM(256, batch_input_shape=(batch, term, features), return_sequences=True))
    model.add(keras.layers.LSTM(256))
    model.add(keras.layers.Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mse')
    return model

def modeling_day7(batch, term, features):
    model = keras.Sequential()
    model.add(keras.layers.LSTM(512, batch_input_shape=(batch, term, features), return_sequences=True))
    model.add(keras.layers.LSTM(512))
    model.add(keras.layers.Dense(7, activation='linear'))
    model.compile(optimizer='adam', loss='mse')
    return model

def model_educate(company, term, batch, predict_day):
    try:
        if predict_day == 1:
            model = company.model_day1
        elif predict_day == 7:
            model = company.model_day7

    except:
        print("Model Setting Error")

    data = company.price
    print(data)
    if company.features == 2:
        data = data[['Date', 'Close', 'Volume']]
    elif company.features == 5:
        data = data[['Date', 'Close', 'Open', 'High', 'Low', 'Volume']]
    # data = method.merge(company.news, company.price, "Date", "Date")
    timeline = pd.to_datetime(data.pop("Date"), format="%Y-%m-%d")
    Scaler = MinMaxScaler(feature_range=(0, 1))
    Scaler.fit(data)
    data = Scaler.fit_transform(data)

    train_data = data

    train_x, train_y = create_dataset(train_data, term, predict_day)

    batch_point = method.re_sizing(batch, train_x)
    train_x = train_x[batch_point:]
    train_y = train_y[batch_point:]

    # early_stop = EarlyStopping(monitor="loss", patience=5)
    # check_point = ModelCheckpoint(filepath="../model/")
    # # history = model.fit(train_x, train_y, epoch=100, batch_size=10, callbacks=[early_stop, check_point])
    if predict_day == 1:
        history = model.fit(train_x, train_y, epochs=30, batch_size=10)
        model.save("../model/" + company.code)
    elif predict_day == 7:
        history = model.fit(train_x, train_y, epochs=30, batch_size=10)
        model.save("../model_day7/" + company.code)
    else:
        print("predict_day Setting Error!")

    return model

def update_model(company):
    model_day1 = company.model_day1
    model_day7 = company.model_day7

    return model_day1, model_day7

def predict_day1(company):
    model = company.model_day1
    data = company.price[-29:]
    data = data[['Date', 'Close', 'Volume']]
    close = list(data['Close'])
    # data = method.merge(company.news, company.price, "Date", "Date")
    timeline = pd.to_datetime(data.pop("Date"), format="%Y-%m-%d")

    Scaler = MinMaxScaler(feature_range=(0, 1))
    Scaler.fit(data)
    normed_data = Scaler.fit_transform(data)
    x_data, y_data = create_dataset(normed_data, 28, 1)
    predictions = model.predict(x_data, batch_size=1)
    real_prediction =method.inverseTransform(Scaler, predictions)

    view_day1(timeline, real_prediction, close, company.name)

    return {'Time': timeline, 'Price': close, 'Predict': real_prediction}

def predict_day7(company):
    model = company.model_day7
    data = company.price[-35:]
    data = data[['Date', 'Close', 'Volume']]
    close = list(data['Close'])
    # data = method.merge(company.news, company.price, "Date", "Date")
    timeline = pd.to_datetime(data.pop("Date"), format="%Y-%m-%d")

    Scaler = MinMaxScaler(feature_range=(0, 1))
    Scaler.fit(data)
    normed_data = Scaler.fit_transform(data)
    x_data, y_data = create_dataset(normed_data, 28, 7)

    predictions = model.predict(x_data, batch_size=1)
    real_prediction = method.inverseTransform(Scaler, predictions)

    view_day7(timeline, real_prediction, close, company.name)

    return {'Time': timeline, 'Price': close, 'Predict': real_prediction}

def view_day1(time, predict, actual, name):
    plt.figure(figsize=(16, 9))
    plt.plot(time[:28], actual[-29:-1], marker=".", label="price")
    plt.scatter(time[28:], actual[-1], label="Actual", edgecolors='k', c='#2ca02c', s=100)
    plt.scatter(time[28:], predict, label="Predict", edgecolors='k', marker='X', c='#ff7f0e', s=100)
    plt.xlabel("Time")
    plt.ylabel("Close Price(￦)")
    plt.title(name+"'s Predicted next day's Close(￦)")
    plt.legend()
    plt.show()

def view_day7(days, predict, actual, name):
    plt.figure(figsize=(16, 9))
    plt.plot(days[:28], actual[:28], marker='.', label="price")
    plt.scatter(days[28:], actual[28:], label="Actual", edgecolors='k', c='#2ca02c', s=100)
    plt.scatter(days[28:], predict, label="Predict", edgecolors='k', marker='X', c='#ff7f0e', s=100)
    plt.xlabel("Time")
    plt.ylabel("Close Price(￦)")
    plt.legend()
    plt.title(name+"'s Predicted next week's Close(￦)")
    plt.show()
