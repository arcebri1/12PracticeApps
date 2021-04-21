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

# url = "https://www.basketball-reference.com/leagues/NBA_" + str(year_to_select) + "_per_game.html"
# html = pd.read_html(url, header = 0)
# df = html[0]
# raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
# raw = raw.fillna(0)
# playerstats = raw.drop(['Rk'], axis=1)
# # url
# # html
# # df
# # raw
# playerstats

team_unique = playerstats.Tm.unique()
# team_unique

# Sidebar - Selected Team
sorted_team_selection = sorted(playerstats.Tm.unique())
# sorted_team_selection
selected_team = st.sidebar.multiselect('Team', sorted_team_selection, sorted_team_selection)

# Sidebar - Selected Position
position_selection = ['C', 'PF', 'SF', 'PG', 'SG']
selected_position = st.sidebar.multiselect('Position', position_selection, position_selection)

# Filtering Data
filter_data_selected = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_position))]
# filter_data_selected

# Diplaying Data Info & Dataframe
st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(filter_data_selected.shape[0]) + ' rows and ' + str(filter_data_selected.shape[1]) + ' columns')
st.dataframe(filter_data_selected)

# Downloading NBA data by defining a function and calling it
# We use the article in README to get this done
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href


st.markdown(filedownload(filter_data_selected), unsafe_allow_html=True)

# Creating Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Map')
    filter_data_selected.to_csv('output.csv', index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7,5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
        st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()



