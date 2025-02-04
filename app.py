import streamlit as st
from content_based_filtering import content_recommendation
from scipy.sparse import load_npz
import pandas as pd
from numpy import load

# load the data
cleaned_data_path = "data/cleaned_data.csv"
songs_data = pd.read_csv(cleaned_data_path)

# load the transformed data
transformed_data_path = "data/transformed_data.npz"
transformed_data = load_npz(transformed_data_path)

# Title
st.title("Welcome to the Spotify Song Recommender")

# subheader
st.write("### Enter the name of a song and the recommder will suggest similar songs.🎵🎧")

# Text Input.
song_name = st.text_input("Enter a song name: ")
st.write("You entered: ", artist_name)

# artist name.
artist_name = st.text_input("Enter the artist name: ")
st.write("You entered: ", artist_name)

# lowercase the input.
song_name = song_name.lower()
artist_name = artist_name.lower()
