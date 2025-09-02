import yfinance as yf
import pandas as pd


df_stock = pd.read_csv("Stock Screener Data 31 Aug 2-16-26.csv.csv")

df_stock["Yahoo_Code"] = df_stock["Code"] + ".SI"


list_stock = []

for index, row in df_stock.iterrows():
    list_stock.append(row["Yahoo_Code"])

print(list_stock)


# data = yf.Ticker("D05.SI")

# print(dat.history(period='5d'))

data = yf.download(list_stock, period='5d')

print(data)

data.to_csv("trial.csv")