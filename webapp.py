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
import time
from multiprocessing import Process 

st.image('https://pbs.twimg.com/profile_images/1523787527441817605/KsVU0iId_400x400.jpg', width=100)

st.title('TradingSense Spotlight')
with st.sidebar:
    st.header("Search")
    ticker_input = st.text_input('Please enter company ticker:')
    search_button = st.button('- Get Signal -')
    
col1,col2,col3,col4 = st.columns(4)

if search_button:
    foo(ticker_input)
    #customdata = pandas.read_csv(r'custom.csv')
    #st.write(customdata)
num = 1
today = date.today()
yesterday = today - timedelta(days = 1)
start = '2022-01-01'      
end = datetime.today().strftime('%Y-%m-%d')
lisp = ['AAPL','TSLA']
h = stocker.predict.tomorrow(lisp[num])[0]
live = si.get_live_price(lisp[num])
customdata = yf.download(lisp[num],start,end)
customframe = StockDataFrame.retype(customdata)
stock = customframe
custommfi = stock.get('mfi')[yesterday.strftime('%Y-%m-%d')].round(2)*100
customwr = stock.get('wr')[yesterday.strftime('%Y-%m-%d')].round(2)

if custommfi < 20:
    customstate = 'Oversold/Undervalued'
elif custommfi > 80:
    customstate = 'Overbought/Overvalued'
else:
    customstate = 'Normal '

if customwr < -80:
    customheight = 'Lower Than Normal'
elif customwr > -20:
    customheight = 'Higher Than Normal'
else:
    customheight = 'Normal'
if customheight == 'Lower Than Normal' and customstate == 'Oversold/Undervalued' and h >= live + 5:
    recc = 'STRONG BUY'
elif customheight == 'Higher Than Normal' and customstate == 'Overbought/Overvalued':
    recc = 'SELL'
elif customheight == 'Lower Than Normal' and customstate == 'Normal ':
    recc = 'BUY'
elif customheight == 'Higher Than Normal' and customstate == 'Normal ' and h >= live + 5:
    recc = 'HOLD'
else:
    recc='HOLD'
        




customdata = yf.download(lisp[num],start,end)
old = customdata['Close'].tail()
old1 = old[2]

col2.header('Price')
header = st.empty()


with col1:
    st.header('Ticker')
    st.header(lisp[num])



with col2:
    numbers = st.empty()
    with numbers.container():
        live = si.get_live_price(lisp[num])
        pastprice = live - old1
        pastprice = round(pastprice,2)
        mertric = st.metric('Price',round(live,2),delta=pastprice)

with col4:
    st.header('Signal')
    st.metric('Signal', recc)       
with col3:
    prev = st.empty()
    z=1
    while z==1:
        
        with prev.container():
            st.header('LTSM Prediction')
            h = stocker.predict.tomorrow(lisp[num])[0]
            difference = h - live
            difference = round(difference,2)
            st.metric('LTSM Forecast(7 day)',h,delta = difference)
            time.sleep(1)




            
st.write('---')

st.write('TradingSense uses machine learning to forecast upcoming stock prices. All data is sourced from Yahoo Finance and used to calculate RSI, MFI, P/E Ratio, and WR indcators.'+
           ' These are used in conjunction to provide trading signals to investors. TradingSense is not responsible for the outcome'+
           ' of trades made on the behalf of information sources on this site or the results of trades using info presented on this site. - TradingSense')
