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
sequence  = ''.join(sequence)
# sequence

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')
def DNA_nucleo_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C',seq.count('C'))
        ])
    return d

X = DNA_nucleo_count(sequence)
X

# x_label = list(X)
# x_values = list(X.values())
# x_label
# x_values

## Have to turn count into a string because you can't concatenate a number
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
# df
df = df.rename({0:'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Nucleotide'})
df

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'Nucleotide',
    y = 'Count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)

p