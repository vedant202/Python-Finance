import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

def visualze_Data():
    df = pd.read_csv("nifty50_joined_closes.csv")
    df_corr = df.corr()
    # print(df_corr.head())
    # print("------------ Tail ------------")
    # print(df_corr.tail(15))

    data1 = df_corr.values
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    heatmap = ax1.pcolor(data1,cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
    ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)

    ax1.invert_yaxis()
    ax1.xaxis.tick_top()

    column_labels = df_corr.columns
    row_label = df_corr.index
    ax1.set_xticklabels(column_labels)
    ax1.set_yticklabels(row_label)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()

    # df.plot(x='Date',y='RELIANCE')
    plt.show()

visualze_Data()
