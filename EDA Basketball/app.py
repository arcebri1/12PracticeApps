import streamlit as st
import pandas as pd
import base64 #handle data download for csv file
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
year_to_select = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))
#This is another way to reverse a list
# another_way_to_do_it=st.sidebar.selectbox('Years', range(2019,1949, -1))

## Web scraping NBA stats


