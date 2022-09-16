from nifty50_Company_list import save_ticker
import os
# import pandas as pd
import pandas_datareader.data as web
import pickle
import datetime as dt

def get_data_Nifty_yahoo(reload_nifty=False):
    if reload_nifty:
        tickers = save_ticker()
    else:
        tickers = []
        with open("nifty50CompanyList.pickel","rb") as f:
            tickers=pickle.load(f)
        if not os.path.exists('nifty50_stocks_df'):
            os.makedirs('nifty50_stocks_df')
        start = dt.datetime(1995,1,1)
        end = dt.datetime(2021,8,23)
        for ticker in tickers:
            print(ticker)
            if not os.path.exists("nifty50_stocks_df/{}.csv".format(ticker)):
                df = web.DataReader(f"{ticker}.NS",'yahoo',start,end)
                df.to_csv("nifty50_stocks_df/{}.csv".format(ticker))
            else:
                print("Already have {}".format(ticker))

get_data_Nifty_yahoo()
        