import streamlit as st
from generator.load_prompt import load_prompt
from generator.execute_prompt import execute_prompt
from prompts.prompt_loader import load_all_prompts


def render_story_page():
    """
    Render the story editor page.
    Displays the current story and allows prompt-based interactions.
    """

    # convenience buttons
    col_left, col_spacer, col_right = st.columns([1, 8, 1])
    with col_left:
        if st.button("⬅️ Back to Templates"):
            st.session_state.page = "select_template"
            st.session_state.story_text = ""
            st.session_state.template_name = ""
            st.rerun()
    with col_right:
        if st.button("🧹 Clear Text"):
            st.session_state.story_text = ""
            st.rerun()

    # page title
    st.markdown(
        f"<h2 style='text-align: center;'>{st.session_state.template_name.title()}</h2>",
        unsafe_allow_html=True
    )

    # Subheading
    st.markdown(
        "<p style='font-size: 0.9rem;'>✍️ Your imagination space to shape the narrative...</p>",
        unsafe_allow_html=True
    )

    # Story text area
    story_text = st.text_area(
        label="",
        value=st.session_state.story_text,
        height=300,
        key="story_text_area",
        label_visibility="collapsed"
    )

    if story_text != st.session_state.story_text:
        st.session_state.story_text = story_text

    # load and display prompt buttons
    all_prompts = load_all_prompts()
    prompt_keys = list(all_prompts.keys())
    
    if prompt_keys:
        # Use more columns to allow compact horizontal layout
        col_count = len(prompt_keys)
        cols = st.columns(col_count)

        for i, prompt_key in enumerate(prompt_keys):
            prompt = all_prompts[prompt_key]
            name = prompt.get("name", prompt_key)
            label = prompt.get("label", prompt_key)
            description = prompt.get("description", "")
            mode = prompt.get("mode", "append")

            with cols[i]:
                # Add spacing around the button using markdown with HTML for padding
                st.markdown("<div style='padding: 0.2rem;'>", unsafe_allow_html=True)
                if st.button(label, help=description, key=f"prompt_{prompt_key}"):
                    with st.spinner(f"Running prompt: {name}"):
                        result = execute_prompt(prompt, st.session_state.story_text)

                        if mode == "append":
                            st.session_state.story_text += " " + result
                        elif mode == "replace":
                            st.session_state.story_text = result
                        else:
                            st.warning(f"Unsupported mode: {mode}")

                        st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
