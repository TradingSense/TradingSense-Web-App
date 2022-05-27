import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from stockstats import StockDataFrame
import yfinance as yf
from datetime import *
from datetime import date
from datetime import timedelta
import time
import dataframe_image as dfi
from yahoo_fin import stock_info as si
import stocker
import re
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import pandas_datareader.data as web

st.title('Signal Search')
    
ticker_input = st.text_input('Please enter company ticker:')
search_button = st.button('- Get Signal -')

def foo(ticker_input):
    day = 1
    weekday = datetime.today().weekday()
    if weekday == 0:
        day = 3
    elif weekday == 6:
        day = 2
    else:
        day = 1
    ticker = ticker_input
    col1,col2,col3 = st.columns(3)

    
    today = date.today()
    yesterday = today - timedelta(days = day)
    start = '2022-01-01'      
    end = datetime.today().strftime('%Y-%m-%d')

    customdata = yf.download(ticker,start,end)
    customframe = StockDataFrame.retype(customdata)
    stock = customframe
    custommfi = stock.get('mfi')[yesterday.strftime('%Y-%m-%d')].round(2)*100
    customwr = stock.get('wr')[yesterday.strftime('%Y-%m-%d')].round(2)

    h = stocker.predict.tomorrow(ticker)[0]
    live = si.get_live_price(ticker)

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

   
    

    difference = h - live
    difference = round(difference,2)
    old = customdata['close'].tail()
    old1 = old[2]
    pastprice = old1 - live
    pastprice = round(pastprice,2)
    live = int(live)
    if difference > 0:
        direction = 'Gain'
    elif difference < 0:
        direction ='Loss'

    col1.metric('Signal',str(recc),delta_color="green")
    col2.metric('Current Price',round(live,2),delta=str(pastprice)+'(24hr)')
    col3.metric('1 Week Forecast Price: ',str(h),delta=str(difference)+'(7 Days)')
    st.write('---')
    st.write('--Signal Indicators--')
    st.write('Williams Percent Range: '+str(customheight))
    st.write('Money Flow Index State: '+str(customstate))
    st.write('Machine Learning Prediction: '+str(direction))



if search_button:
    foo(ticker_input)




