# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:21:53 2023

@author: 91999
"""

import streamlit as st
from PIL import Image

def greyscale(image):
    return image.convert('L')

st.title("Greyscale Image Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open("image.jpg")
    st.image(image, caption='Original Image', use_column_width=True)
    if st.button('Convert to Greyscale'):
        greyscale_image = greyscale(image)
        st.image(greyscale_image, caption='Greyscale Image', use_column_width=True)



