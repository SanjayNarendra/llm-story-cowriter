import streamlit as st
from generator.execute_prompt import execute_prompt
from templates.template_loader import load_all_templates


def render_template_page():
    """
    Render the template selection page
    """
    # page title and caption
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 0;">
            <h1 style="font-family: Cinzel, serif; font-size: 4rem; margin-bottom: 0;">
                Futuring Machines
            </h1>
            <p style="color: #aaa; font-size: 1rem; margin-top: 0; margin-left: 20rem;">
                A story whispered by you, echoed by AI ✨
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h5 style='font-family: Segoe UI, sans-serif; font-size: 1.1rem; margin: 2.5rem 0rem 0.4rem;'>
            Choose a setting to begin your story:
        </h5>
        """,
        unsafe_allow_html=True
    )

    # templates selection
    all_templates = load_all_templates()

    # Render buttons for each template
    for key, template in all_templates.items():
        label = template.get("label", key)
        description = template.get("description", "")

        if st.button(label, help=description, key=f"template_btn_{key}"):
            action = template.get("actions", [{}])[0]
            action_type = action.get("type", "")

            if action_type == "static":
                story_text = action.get("template", "")
            elif action_type == "generate":
                with st.spinner("Story loading..."):
                    story_text = execute_prompt(template, "")
            else:
                story_text = "[Invalid template format]"

            st.session_state.story_text = story_text
            st.session_state.template_name = template.get("name", key)
            st.session_state.page = "write_story"
            st.rerun()
                

        
