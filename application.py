import streamlit as st
from PIL import Image

def rgb_to_gray(image):
    gray = image.convert('L')
    return gray

st.header('Greyscale convertor 🔗')
st.write("This Grayscale Image Converter app is a user-friendly tool designed to convert color images(RGB) to grayscale. Powered by Streamlit, a Python library for creating interactive web applications, this app allows users to upload their image files and instantly view the grayscale version.")

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original RGB Image', use_column_width=True)

    if st.button('Convert to Greyscale'):
        gray_image = rgb_to_gray(image)
        st.image(gray_image, caption='Converted Greyscale Image', use_column_width=True)

