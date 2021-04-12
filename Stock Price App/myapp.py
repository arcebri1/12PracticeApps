import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Below is Google's stock information for May 31 2010-2020

""")

#To obtain the stock info we gathered the info from the article Towards Data Science that can be found in the README file
tickerSymbol = 'GOOGL'
# st.write(tickerSymbol)

tickerData = yf.Ticker(tickerSymbol)
# st.write(tickerData)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write(tickerDf)

st.write("""

## Google's Stock Closing Price for May 31 2010-2020

""")
st.line_chart(tickerDf.Close)

st.write("""

## Google's Stock Volume Price for May 31 2010-2020

""")
st.line_chart(tickerDf.Volume)