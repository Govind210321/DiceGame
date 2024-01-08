import navlog
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2 
import mediapipe as mp 
from keras.models import load_model
import base64

st.set_page_config(
    page_title="Emotional Based Music",
   # page_icon="👋",
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
st.header("Welcome To ")
st.header("Expression Based Music Player")
#st.header("final year project")

if "run" not in st.session_state:
	st.session_state["run"] = "true"

if "step2" not in st.session_state:
	st.session_state["step2"] = "false"


import time
def progress():
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1, text=progress_text)
	

def stage1():
    btn1 = st.button("capture the image ")

    if btn1 and st.session_state["run"] == "true":

        progress()
        st.session_state["step2"] = "true"
        navlog.nav_page("stage2")
        
from streamlit.components.v1 import html

    

#print(btn1, st.session_state["run"])
stage1()

