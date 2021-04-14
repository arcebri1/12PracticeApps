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


@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(year_to_select)

url = "https://www.basketball-reference.com/leagues/NBA_" + str(year_to_select) + "_per_game.html"
html = pd.read_html(url, header = 0)
df = html[0]
raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
raw = raw.fillna(0)
playerstats = raw.drop(['Rk'], axis=1)
# url
# html
# df
# raw
playerstats

team_unique = playerstats.Tm.unique()
team_unique

sorted_team_selection = sorted(playerstats.Tm.unique())
sorted_team_selection

selected_team = st.sidebar.multiselect('Team', sorted_team_selection, sorted_team_selection)

position_selection = ['C', 'PF', 'SF', 'PG', 'SG']
selected_position = st.sidebar.multiselect('Position', position_selection, position_selection)

filter_data_selected = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_position))]
filter_data_selected



