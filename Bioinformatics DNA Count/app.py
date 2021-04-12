import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna2.jpg')

st.image(image, use_column_width = True)

st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
# sequence_input

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
# sequence
sequence = sequence[1:]
# sequence


