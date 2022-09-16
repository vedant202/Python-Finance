import pickle
import pandas as pd
import datetime as dt

def compile_data():
    tickers = []
    with open("nifty50CompanyList.pickel","rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()
    for count,ticker in enumerate(tickers):
        df = pd.read_csv('nifty50_stocks_df/{}.csv'.format(ticker))
        df.set_index('Date',inplace=True)
        
        df.rename(columns={'Adj Close':ticker},inplace=True)
        df.drop(['Open','High','Low','Close','Volume'],axis=1,inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,how='outer')

        if count %5==0:
            print(count)

        print(main_df.head())
        main_df.to_csv('nifty50_joined_closes.csv')
if __name__=="__main__":
    # compile_data()
    df = pd.read_csv("nifty50_joined_closes.csv")
    # print(df.head(50))
    print(df.tail(50))
    

    