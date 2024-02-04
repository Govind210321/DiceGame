import navlog
from streamlit_webrtc import webrtc_streamer
import streamlit as st
from emopro import *

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


if st.session_state["step2"] == "true":

    webrtc_streamer(key="key", 
        desired_playing_state=True, 
        sendback_audio=False,
        video_processor_factory=EmotionProcessor)
    btn3 = st.button("next")

    if btn3:
        try:
            emotion = np.load("emotion.npy")[0]
        except:
            emotion=""
        print('emotion', emotion)
        st.session_state["emotion"]=emotion
        navlog.nav_page("stage3")
    
