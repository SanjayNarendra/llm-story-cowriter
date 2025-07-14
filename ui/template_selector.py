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
        <div style="margin: 2.5rem 0 0rem 10rem;">
            <h5 style='font-family: Segoe UI, sans-serif; font-size: 1.1rem;'>
                Choose a setting to begin your story:
            </h5>
        </div>
        """,
        unsafe_allow_html=True
    )

    # templates selection
    all_templates = load_all_templates()

    # Render buttons for each template
    for key, template in all_templates.items():
        label = template.get("label", key)
        description = template.get("description", "")

        with st.container():
            st.markdown("<div style='max-width: 70%;  margin-left: 4rem; margin-bottom: 0.5rem;'>", unsafe_allow_html=True)
            col_text, col_button = st.columns([1, 1])

            with col_text:
                st.markdown(f"""
                    <div style="padding: 1rem 10rem; border: 1px solid #333; border-radius: 2rem; text-align: center;
                                background-color: #1e1e1e;">
                        <div style="font-size: 1.5rem; font-weight: 600; margin-bottom: 0.4rem;">{label}</div>
                        <div style="font-size: 1rem; color: #aaa;">{description}</div>
                    </div>
                """, unsafe_allow_html=True)

            with col_button:
                st.markdown("<div style='margin-top: 2.2rem;'>", unsafe_allow_html=True)
                if st.button("📖 Let's Begin", key=f"launch_{key}"):
                    action = template.get("actions", [{}])[0]
                    action_type = action.get("type", "")

                    if action_type == "static":
                        story_text = action.get("template", "")
                    elif action_type == "generate":
                        with st.spinner("Loading your story..."):
                            story_text = execute_prompt(template, "")
                    else:
                        story_text = "[Invalid template format]"

                    st.session_state.story_text = story_text
                    st.session_state.template_name = template.get("name", key)
                    st.session_state.page = "write_story"
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)
                

        
