import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# end = dt.datetime(2021,8,20)
# start = dt.datetime(2001,1,1)

# df = web.DataReader('TATAMOTORS.NS','yahoo',start,end)

# print(df.tail(10))
# df.to_csv('TATAMOTORS1.csv')

df = pd.read_csv("TATAMOTORS1.csv",parse_dates=True,index_col=0)
print(df.tail(10))
df['Adj Close'].plot(label='Adjecent price')
plt.xlabel('years')
plt.ylabel('price (RS)')
plt.show()