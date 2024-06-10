# slider_script.py
import streamlit as st
from PIL import Image
import os

def slider_app():

    # CSS to hide the tick labels below the slider and the current value
    st.markdown("""
        <style>
        /* Hide the tick labels below the slider */
        .stSlider div[data-testid="stTickBar"] > div {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)
    
    images = [
        {"title": "Número de caminhadas", "file": "content/Assets/section1/image1.png"},
        {"title": "Satisfação utilizadores", "file": "content/Assets/section1/image2.png"},
        {"title": "Esperança de vida em Vale Sereno", "file": "content/Assets/section1/image3.png"},
        {"title": "Gastos públicos em saúde", "file": "content/Assets/section1/image4.png"}
    ]

    # Create the select slider
    slider_labels = [img["title"] for img in images]
    slider_value = st.select_slider("Importância do acesso a dados", label_visibility="hidden", options=slider_labels)

    # Find the index of the selected label
    selected_index = slider_labels.index(slider_value)
    image_info = images[selected_index]

    # Display the image based on the slider value
    image = Image.open(image_info["file"])
    st.image(image, use_column_width=True)

# Ensure the script can be run standalone for testing
if __name__ == "__main__":
    slider_app()
