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

picks = ['AAPL','AMZN','TSLA','XOM','BA']

## -- ## -- Get state values --
today = date.today()


start = '2022-01-01'      
end = datetime.today().strftime('%Y-%m-%d')

  
    
st.write('---')







def foo(ticker):
    today = date.today()

    yesterday = today - timedelta(days = 4)


    start = '2022-01-01'      
    end = datetime.today().strftime('%Y-%m-%d')

    customdata = yf.download(ticker,start,end)
    customframe = StockDataFrame.retype(customdata)
    stock = customframe
    custommfi = stock.get('mfi')[yesterday.strftime('%Y-%m-%d')].round(2)*100
    customwr = stock.get('wr')[yesterday.strftime('%Y-%m-%d')].round(2)

    h = stocker.predict.tomorrow(ticker)[0]
    live = si.get_live_price(ticker)
    other = si.get_quote_table(ticker)

    
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

    col1, col2, col3,col4 = st.columns(4)
    
    tickerSymbol = ticker
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='id', start='2020-5-31', end=datetime.today().strftime('%Y-%m-%d'))
    difference = h - live
    difference = round(difference,2)
    old = customdata['close'].tail()
    old1 = old[2]
    pastprice = old1 - live
    pastprice = round(pastprice,2)
    if difference > 0:
        direction = 'Gain'
    elif difference < 0:
        direction ='Loss'

    col3.metric('Price to Earnings Ratio: ', str(other["PE Ratio (TTM)"]))
       
    col2.metric('1 Week Forecast Price: ',str(h),delta=difference)
    col2.metric('Williams Percent Range: ', str(customwr))
    col3.metric('Money Flow Index: ',str(custommfi))
    col1.metric('Current Price',round(live,2),delta=str(pastprice)+'(24hr)')
    col1.metric('Signal',recc,delta_color="green")
    col1.header('Signal Indicators')
    col2.write('---')
    col2.write('Earnings Per Share: '+str(other['EPS (TTM)']))
    col2.write('Volume: '+str(other['Volume']))
    col2.write('Market Cap: '+str(other['Market Cap']))
    col1.write('Williams Percent Range: '+str(customheight))
    col1.write('Money Flow Index State: '+str(customstate))
    col1.write('Machine Learning Prediction: '+str(direction))
    col4.line_chart(tickerDf.Close)

def losers():
    si.get_day_losers()
    
def gainers():
    si.get_day_gainers()
    
