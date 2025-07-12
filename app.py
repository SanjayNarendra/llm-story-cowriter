import streamlit as st
from generator.load_template import load_template
from generator.load_prompt import load_prompt
from generator.generate_text import generate_text


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

# load template and prompt
template = load_template('futuristicCity')
prompt = load_prompt('continueWriting')

# initialize story
if "story" not in st.session_state:
    st.session_state.story = template.get("template", "")

# story text area
story = st.text_area("✍️ Your Imagination Space", value=st.session_state.story, height=400)

# continue story with LLM
if st.button("✨ Continue Story"):
    generated = generate_text(prompt, story)
    st.session_state.story += "\n" + generated
    st.rerun()

