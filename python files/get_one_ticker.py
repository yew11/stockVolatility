from clean import *
from pandas_datareader.data import Options

def get_one_ticker(one_ticker_name):
    option_data = Options(one_ticker_name,data_source='yahoo').get_all_data()
    option_data.reset_index(inplace=True)
    option_data.drop('JSON', axis=1, inplace=True)
    r=clean(option_data)
    return r