import streamlit as st
import pandas as pd
import numpy as np
import pickle 



songs = pickle.load(open('song.pkl', 'rb'))
song_list = pd.DataFrame(songs)


similarity = pickle.load(open('similarity.pkl', 'rb'))
singer = pickle.load(open('singer.pkl', 'rb'))


def recommend(song):
    index = song_list[song_list['title'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_songs = []
    recommended_videos = []
    for i in distances[1:6]:
        recommended_songs.append(song_list.iloc[i[0]].title)
        recommended_videos.append(youtube(song_list.iloc[i[0]].title))
    return recommended_songs, recommended_videos


def youtube(song):
    index = song_list[song_list['title'] == song].index[0]
    singer_name = singer[index]
    songs = song + ' by ' + singer_name
    songs = songs.replace(' ', '+')
    #use of link to get the video
    response = 'https://www.youtube.com/results?search_query={songs}'.format(songs=songs)
    return response



st.title("Song Recommender System")

selected_song = st.selectbox(
    'Discover your next favorite tune with a harmonious search.',
    #return song_list['title'].values and list(singerz) together as a list
     
    (song_list['title'].values) ) 



if st.button('Exploreeee'):
    st.write('Recomended Songs:')
    name, video = recommend(selected_song)
    for i in range(len(name)):
        with st.expander(f'{name[i]}'):
            st.write('Click on the link to listen to the song')
            st.write(video[i])

