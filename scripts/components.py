# helpers/ui_helpers.py
import streamlit as st
import os
import json


def render_static_content(section):
    """Render title, image, and text from the section."""
    if "title" in section:
        st.header(section["title"])
    if "image_path" in section and os.path.exists(section["image_path"]):
        st.image(section["image_path"])
        st.divider()
    if "text" in section:
        st.markdown(section["text"].replace("\n", "  \n"))

def render_question_content(section):
    """Render question and handle user response."""
    question_key = "question_multiple" if "question_multiple" in section else "question"
    if question_key in section:
        st.write(section[question_key])
        options = section.get("options", [])
        selected_options = st.multiselect("Selecione uma ou mais opções", options) if question_key == "question_multiple" else st.radio("Selecione uma opção", options)

        if selected_options:
            if "response_submitted" not in st.session_state:
                st.session_state.response_submitted = False

            if not st.session_state.response_submitted:
                if st.button(section.get("button_text", "Responder")):
                    st.session_state.response_submitted = True
                    if set(selected_options) == set(section.get("answer", [])):
                        st.success("Correcto!")
                    else:
                        st.error("Errado!")

            if st.session_state.response_submitted:
                st.write(section["explanation"])
                st.subheader('', divider='rainbow')
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(section.get("button_answer", "Continuar")):
                        st.session_state.current_section += 1
                        st.session_state.response_submitted = False
                        st.rerun()
                if st.session_state.current_section > 0:
                    with col2:
                        if st.button("Voltar"):
                            st.session_state.current_section -= 1
                            st.session_state.response_submitted = False
                            st.rerun()



def render_script_content(section):
    """Execute script if present in the section."""
    if "script_path" in section:
        script_path = section["script_path"]
        script_dir, script_name = os.path.split(script_path)
        script_module_name = script_name.replace('.py', '')

        # Add script directory to the system path
        import sys
        sys.path.append(script_dir)

        # Import and run the script
        script_module = __import__(script_module_name)
        script_module.slider_app()

        st.write(section["explanation"])

def render_navigation_buttons(section):
    """Render navigation buttons."""
    if "button_text" in section:
        if st.session_state.current_section > 0:
            st.subheader('', divider='rainbow')
            col1, col2 = st.columns(2)
            with col1:
                if st.button(section["button_text"]):
                    st.session_state.current_section += 1
                    st.rerun()
            with col2:
                if st.button("Voltar"):
                    st.session_state.current_section -= 1
                    st.rerun()
        else:
            if st.button(section["button_text"]):
                st.session_state.current_section += 1
                st.rerun()

def load_quiz_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

