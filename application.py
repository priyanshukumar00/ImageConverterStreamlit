import streamlit as st
from PIL import Image

def rgb_to_gray(image):
    gray = image.convert('L')
    return gray

st.title('Greyscale convertor')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original RGB Image', use_column_width=True)

    if st.button('Convert to Greyscale'):
        gray_image = rgb_to_gray(image)
        st.image(gray_image, caption='Converted Greyscale Image', use_column_width=True)

