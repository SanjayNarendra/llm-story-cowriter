import streamlit as st
from generator.load_template import load_template
from generator.load_prompt import load_prompt


st.set_page_config(page_title='Futuring Machines', layout="centered")

st.title("Futuring Machines - Let's imagine the future together")
st.markdown(
    """
    <h4 style='text-align: right; color: #aaa; font-weight: 400; font-size: 18px;'>
        A story whispered by you, echoed by AI ✨
    </h4>
    """,
    unsafe_allow_html=True
)

# load template 
template = load_template('futuristicCity')

# initialize story
if "story" not in st.session_state:
    st.session_state.story = template.get("template", "")

# text area for user to write/edit story
story = st.text_area("✍️ Your Imagination Space", value=st.session_state.story, height=400)

