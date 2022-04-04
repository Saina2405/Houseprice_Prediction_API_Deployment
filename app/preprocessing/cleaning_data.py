''' This function preprocess() takes an information of a house as input and return those
    preprocessed information as output.'''

import pandas as pd
import pickle
import numpy as np


model_columns = pickle.load(open('./model/model_columns.pkl', 'rb'))


def convert_to_binary(data, category):
    # print("HERRRRR")
    # print(f"{category = }")
    # print("HERRRRR")
    # print(f"{data['data'] =}")
    # print(data[category])
    # print(f"convert_to_binary{data = }")
    if data["data"][category] == "True":
        return 1
    else:
        return 0

def preprocess(data):
    """
    Clean data to be suitable for model requirements
    """
    print("**********")
    print(f"{list(model_columns) = }")
    # print("**********")
    # print(f"{data =}")

    # Check valid input & convert in data for model for building_condition
    building_condition_dictionary = {
        'As new': 6,
        'Just renovated': 5,
        'Good': 4,
        'To be done up': 3,
        'To renovate': 2,
        'To restore': 1
    }

    data["data"]["Building condition"] = building_condition_dictionary.get(data["data"]["Building condition"], 0)
  
    # Check valid input & convert in data for model for kitchen_type
    kitchen_type_dictionary = {
        "USA uninstalled": 0,
        "Not installed": 0,
        "Installed": 1,
        "USA installed": 1,
        "Semi equipped": 1,
        "USA semi equipped": 1,
        "Hyper equipped": 2,
        "USA hyper equipped": 2
    }
    

    data["data"]["Kitchen type"] = kitchen_type_dictionary.get(data["data"]["Kitchen type"], 0)

    # Convert Furnished to binary
    data["data"]["Furnished"] = convert_to_binary(data, "Furnished")

    # Convert Terrace to binary
    data["data"]["Terrace"] = convert_to_binary(data, "Terrace")

    # Convert Garden to binary
    data["data"]["Garden"] = convert_to_binary(data, "Garden")

    # Convert data to a dataframe to one hot encode variables
    # Add columns present in model columns but not data dataframe
    df = pd.DataFrame(data["data"], index=[0])

    # One Hot Encoding of categorial variables like property type, property sub-type, City

    df = pd.get_dummies(df, columns=["Property type", "City"])

    print(df.head(1))
    df = df.reindex(columns=model_columns, fill_value=0)

    return df

