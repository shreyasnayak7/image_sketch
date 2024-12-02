import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Streamlit App Title
st.title("Image to Sketch Converter")
st.write("Upload an image, and this app will convert it into a pencil sketch!")

# Upload Image
uploaded_file = st.file_uploader("E:\image\img.jpeg", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display Original Image
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)

    # Convert to OpenCV format
    image = np.array(image)

    # Process the Image to Create a Sketch
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # Convert to grayscale
    inverted_image = cv2.bitwise_not(gray_image)         # Invert the grayscale image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)  # Apply Gaussian Blur
    inverted_blurred = cv2.bitwise_not(blurred_image)    # Invert the blurred image
    sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)  # Create the sketch

    # Display the Sketch
    st.image(sketch, caption='Pencil Sketch', use_column_width=True)