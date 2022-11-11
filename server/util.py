import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimates_price(location, sqft, bath, balcony, bhk):
    load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print('loading saved artifacts...')
    global __locations
    global __data_columns

    with open("./server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]
    with open("./server/artifacts/banglore_house_price_prediction.pickle", 'rb') as f:
        global __model
        __model = pickle.load(f)
    print('artifacts loaded')


def get_location_names():
    load_saved_artifacts()
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == "__main__":
    print(get_location_names())
