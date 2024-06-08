import streamlit as st
import json
import os

def run():
    st.set_page_config(
        page_title="Análise de avaliabilidade",
        page_icon="🎓",
    )

    # CSS personalizado para os botões
    st.markdown("""
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

    ### Sidebar
    st.sidebar.title("Micro-aprendizagem sobre Análise da avaliabilidade de políticas 🎓")
    st.sidebar.divider()
    st.sidebar.markdown("""Nesta atividade iremos ficar a compreender o conceito de análise de avaliabilidade nas seguintes dimensões: \n
    - Qual a sua função
    - Quais as vantagens
    - Como se operacionaliza
    """)
    st.sidebar.divider()
    st.sidebar.markdown("[Ver guia de avaliabilidade](https://planapp.gov.pt/wp-content/uploads/2024/01/PlanAPP_Guia-Avaliabilidade-1.pdf) 📘")
    st.sidebar.divider()
    st.sidebar.markdown("[Acompanhe o PlanAPP](https://linktr.ee/planapp) 🫶")

    # Inicializar o estado da aplicação
    if 'current_section' not in st.session_state:
        st.session_state.current_section = 0

    # Carrega os dados do quiz
    with open('content/sections_structure.json', 'r', encoding='utf-8') as f:
        section_structure = json.load(f)

    def render_section(section):
        if "title" in section:
            st.header(section["title"])
        if "image_path" in section and os.path.exists(section["image_path"]):
            st.image(section["image_path"])
            st.divider()
        if "text" in section:
            st.markdown(section["text"].replace("\n", "  \n"))
        if "question_multiple" in section or "question" in section:
            question_key = "question_multiple" if "question_multiple" in section else "question"
            st.write(section[question_key])
            options = section.get("options", [])
            selected_options = st.multiselect("Selecione as opções", options) if question_key == "question_multiple" else st.radio("Selecione uma opção", options)

            if selected_options:
                if "response_submitted" not in st.session_state:
                    st.session_state.response_submitted = False

                if not st.session_state.response_submitted:
                    if st.button(section.get("button_text", "Responder")):
                        st.session_state.response_submitted = True
                        if set(selected_options) == set(section.get("answer", [])):
                            st.success("Correcto!")
                        else:
                            st.error("Quase certo!")

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
            else:
                st.warning("Selecione pelo menos uma opção.")

        # Botões para continuar e voltar sem perguntas
        elif "button_text" in section:
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

    # Renderizar a secção atual
    current_section = st.session_state.current_section

    if current_section < len(section_structure):
        render_section(section_structure[current_section])
    else:
        st.markdown(f"""
            <div style="text-align: center;">
                <h3> 🎓Parabéns! Você concluiu a micro-aprendizagem sobre análise de avaliabilidade. 🎓</h3>
            </div>
            """, unsafe_allow_html=True)
        st.subheader('', divider='rainbow')
        st.image("content/Assets/endsection.png")
        st.subheader('', divider='rainbow')
        st.markdown(f"""
            <div style="text-align: center;">
                <h4>Acompanhe o trabalho do PlanAPP em <a href='https://linktr.ee/planapp' target='_blank'>diferentes plataformas</a>.</h4>
            </div>
            """, unsafe_allow_html=True)
        st.balloons()

        # Botão para reiniciar
        if st.button("Reiniciar"):
            st.session_state.current_section = 0
            st.rerun()

if __name__ == "__main__":
    run()
