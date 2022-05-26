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



        




