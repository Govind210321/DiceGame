import streamlit as st
import numpy as np 
import webbrowser

from streamlit_player import st_player

import base64

st.set_page_config(
    page_title="Emotional Based Music",
    page_icon="👋",
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
set_background('bgm.jpg')    

st.header("Expression Based Music Player")
# st.header("final year project")



lang = st.session_state["lang"]

emotion = np.load(r"C:\Users\govin\OneDrive\Documents\Desktop\chanti project\emotion.npy")[0]
#emotion = np.load(r"F:\Downloads\mpro (1)\mpro\emotion.npy")[0]
#emotion = 'happy' #	st.session_state["emotion"]

btn1 = st.button("Recommend me youtube video")

if btn1:
    webbrowser.open(f"https://www.youtube.com/results?search_query={lang}+{emotion}+song")
    #st_player("https://youtu.be/CmSKVW1v0xM")
    #np.save("emotion.npy", np.array([""]))
    st.session_state["run"] = "false"

btn2 = st.button("Recommend me spotify music")

if btn2:
    webbrowser.open(f"https://open.spotify.com/search/{lang}%20{emotion}")
    #st_player("https://soundcloud.com/imaginedragons/demons")
    #np.save("emotion.npy", np.array([""]))
    st.session_state["run"] = "false"

btn4 = st.button("Recommend me local music ")

def playother():
    st.audio(st.session_state.song)

if btn4:
    #webbrowser.open(f"https://open.spotify.com/search/{lang}%20{emotion}")
    mysongs={
        "english":{"happy":["Adele-Hello.mp3", "Marshmello Happier.mp3", "Kygo Happy Now.mp3"], 
                   "sad":["CelineDion-MyHeartWillGoOn.mp3","Sad SongsMp3.Co.mp3","sad2 mp3.Co.mp3"], "surprise":[], "angry":[]}, 
        "telugu":{"happy":["[iSongs.info] 06 - Naatho Vasthava.mp3", "Nee Paata Madhuram - SenSongsmp3.Co.mp3","01 - Asale Pilla - SenSongsMp3.co.mp3"], 
                  "sad":["[iSongs.info] 05 - Amma Amma Neevennela.mp3", "2-Oorikey Ala-SenSongsMp3.Co.mp3", ""], 
                  "surprise":[], "angry":[]}, 
        "hindi":{"happy":["03 - Happy Birthday.mp3","happy_song1.mp3"], 
                 "sad":["Jeena Jeena_64-(PagalWorld.Ink).mp3"," "], 
                 "surprise":[], "angry":[]}, 
         }
    playlist = mysongs[lang][emotion]
    print(playlist)
    #playlist = mysongs["telugu"]["happy"]
    #st_player("https://soundcloud.com/imaginedragons/demons")
    #np.save("emotion.npy", np.array([""]))
    st.session_state["run"] = "false"

    #playlist = m3u_to_list("songs.m3u")
    song = st.selectbox("Pick an MP3 to play", playlist, 0, on_change=playother, key='song')
    st.audio(song)

import streamlit as st

def m3u_to_list(filename):
    out = []
    with open(filename) as fh:
        for line in fh.read().split("\n"):
            line = line.strip()
            if not line.startswith("#"):
                out.append(line)
    return out





