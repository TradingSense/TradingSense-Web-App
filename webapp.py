import streamlit as st
st.set_page_config(page_title='TradingSense', page_icon=None, layout="wide", initial_sidebar_state="auto")
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
from datafile import gainers
from datafile import losers
from e import markdown1
st.warning('Market Is Closed On Weekends, Data not available for weekends')
st.title('TradingSense')
col1,col2,col3,col4 = st.columns(4)
ticker_input = col1.text_input('Please enter company ticker:')
search_button = col1.button('- Search -')


if search_button:
    foo(ticker_input)
    #customdata = pandas.read_csv(r'custom.csv')
    #st.write(customdata)
st.spinner('Building DataFrame')
st.write('---')
col3.write('Days Largest Gainers')
fiver = gainers()
col3.write(str(fiver))
col4.write('Days Largest Losers')
lose=losers()
col4.write(str(lose))
st.image('https://pbs.twimg.com/profile_images/1523787527441817605/KsVU0iId_400x400.jpg', width=100)



