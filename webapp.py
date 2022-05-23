import streamlit as st
st.set_page_config(page_icon=None, layout="wide")
from yahoo_fin import stock_info as si
import pandas as pd
import matplotlib.pyplot as plt
from stockstats import StockDataFrame
import yfinance as yf
from datetime import date
from datetime import timedelta
import datetime as dt
import dataframe_image as dfi
from yahoo_fin import stock_info as si
import stocker
import re
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import pandas_datareader.data as web
import pandas
from datafile import foo
import csv
from datetime import *
st.image('https://pbs.twimg.com/profile_images/1523787527441817605/KsVU0iId_400x400.jpg', width=100)

st.title('TradingSense')
col1,col2,col3,col4 = st.columns(4)
ticker_input = col1.text_input('Please enter company ticker:')
search_button = col1.button('- Get Signal -')

if search_button:
    foo(ticker_input)
    #customdata = pandas.read_csv(r'custom.csv')
    #st.write(customdata)


uno=si.get_day_most_active()
uno1 = uno.head()
uno1.to_csv('dataframe.csv')
content = pandas.read_csv('dataframe.csv')
content = content[['Symbol','% Change']].values


st.write('---')

col4.write('Todays Watchlist')
col4.write(content)

gain = si.get_day_gainers()
gain = gain[['Symbol','% Change']].head()
loser = si.get_day_losers()
loser = loser[['Symbol','% Change']].head()


col2.write('Todays Top Gainers')
col2.write(gain)
col3.write('Todays Top Losers')
col3.write(loser)
st.write('TradingSense uses machine learning to forecast upcoming stock prices. All data is sourced from Yahoo Finance and used to calculate RSI, MFI, P/E Ratio, and WR indcators.'+
           ' These are used in conjunction to provide trading signals to investors. TradingSense is not responsible for the outcome'+
           ' of trades made on the behalf of information sources on this site or the results of trades using info presented on this site. - TradingSense')
