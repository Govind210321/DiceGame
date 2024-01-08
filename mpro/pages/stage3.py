import streamlit as st
import navlog
# lang = st.text_input("Language")

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
#st.header("final year project")


lang = st.selectbox("plz choose language", ("english", "telugu", "hindi") )
st.session_state["lang"] = lang

btn4 = st.button("next")

if btn4:
    navlog.nav_page("stage4")

