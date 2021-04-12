import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna2.jpg')

st.image(image, use_column_width = True)