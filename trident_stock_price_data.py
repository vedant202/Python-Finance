import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import os


start = dt.datetime(2017,10,20)
end = dt.datetime(2021,8,23)

df = web.DataReader("TRIDENT.NS",'yahoo',start,end)

print(df.head(10))
df.to_csv('Trident_stock.csv')