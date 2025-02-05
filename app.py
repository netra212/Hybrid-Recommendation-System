import streamlit as st
from content_based_filtering import recommend
from scipy.sparse import load_npz
import pandas as pd
from numpy import load

# load the data
cleaned_data_path = "data/cleaned_data.csv"
# songs_data = pd.read_csv(cleaned_data_path)

# load the transformed data
transformed_data_path = "data/transformed_data.npz"
transformed_data = load_npz(transformed_data_path)

# Loading the main data. 
data = pd.read_csv(cleaned_data_path)

# Title
st.title("Welcome to the Spotify Song Recommender")

# subheader
st.write("### Enter the name of a song and the recommder will suggest similar songs.🎵🎧")

# Text Input.
song_name = st.text_input("Enter a song name: ")
song_name = song_name.lower()
st.write("You entered: ", song_name)

# artist name.
# artist_name = st.text_input("Enter the artist name: ")
# st.write("You entered: ", artist_name)

# lowercase the input.
# artist_name = artist_name.lower()

# k recommendation.
k = st.selectbox("How many recommendations do you want ?", [5, 10, 15, 20], index=1)

# Button. 
if st.button("Get Recommendations"):
    if (data["name"] == song_name).any():
        st.write("Recommendations for ", f"**{song_name}**")
        recommendations = recommend(song_name, data, transformed_data, k)

        # Display Recommendation.
        for index, recommendation in recommendations.iterrows():
            song_name = recommendation["name"].title()
            # artist_name = recommendation["artist"].title()

            if index == 0:
                st.markdown("## Currently Playing")
                st.markdown(f"## **{song_name}** by **{artist_name}")
                st.audio(recommendation["spotify_preview_url"])
                st.write("------")

            elif index == 1:
                st.markdown("### Next up 🎵")
                st.markdown(f"### {index}. **{song_name}** by **{artist_name}**")
                st.audio(recommendation["spotify_preview_url"])
                st.write("------")
            
            else:
                st.markdown(f"### {index}. **{song_name}** by **{artist_name}**")
                st.audio(recommendation["spotify_preview_url"])
                st.write("------")
        
        else:
            st.write(f"Sorry, we could not find {song_name} in our database.Please try another song.")
