import bs4 as bs
import pickle
import requests

def save_ticker():
    resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50',"lxml")
    resp_text = bs.BeautifulSoup(resp.text)
    tabel = resp_text.find("table",{'id':'constituents'})
    # print(tabel)
    tickers = []
    for row in tabel.find_all('tr')[1:]:
        tickers.append(row.find_all('td')[1].text)
    with open("nifty50CompanyList.pickel","wb") as f:
        pickle.dump(tickers,f)
    return tickers
# save_ticker()
obj = []
with open("nifty50CompanyList.pickel","rb") as f:
    obj = pickle.load(f)
# print(obj)
