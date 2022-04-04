''' This function prediction() will take your preprocessed data as input and return a price as output'''

import pickle
import pandas as pd


def prediction(data):
    """
    Use model and prepped dataframe to predict property price
    """

    model = pickle.load(open('./model/model.pkl', 'rb'))
    print(data)
    price = round(model.predict(data)[0], 2)

    return price