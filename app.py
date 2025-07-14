import streamlit as st
from ui.template_selector import render_template_page
from ui.story_editor import render_story_page

# App config
st.set_page_config(page_title="Futuring Machines", layout="wide")

# Session State Setup
if "page" not in st.session_state:
    st.session_state.page = "select_template"

if "story_text" not in st.session_state:
    st.session_state.story_text = ""

if "template_name" not in st.session_state:
    st.session_state.template_name = ""


if st.session_state.page == "select_template":
    render_template_page()
elif st.session_state.page == "write_story":
    render_story_page()

