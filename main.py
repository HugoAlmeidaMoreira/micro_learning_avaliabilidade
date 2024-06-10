import streamlit as st
from components import render_static_content, render_question_content, render_script_content, render_navigation_buttons
from helpers.data_helpers import load_quiz_data

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
    section_structure = load_quiz_data('content/sections_structure.json')

    def render_section(section):
        render_static_content(section)
        render_question_content(section)
        render_script_content(section)
        render_navigation_buttons(section)

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
