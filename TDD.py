import streamlit as st
from PIL import Image
import numpy as np
from tdd.models import predict_image

# Set page title and header
st.set_page_config(page_title="Disease Prediction", page_icon="🩺")
st.title("🌿 Disease Detection from Image")

st.write("Upload an image of a leaf, and the model will predict the disease, if any.")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])


if uploaded_file is not None:
    st.image(uploaded_file, caption='🌱 Uploaded Image', use_column_width=True)

    image = Image.open(uploaded_file)
    img = np.array(image)
    img = np.expand_dims(img, 0)

    try:
        with st.spinner('⏳ Analyzing the image...'):
            class_name, confidence = predict_image(img)

        st.success(f"**Prediction:** {class_name}")
        st.info(f"**Confidence Level:** {confidence}%")

    except Exception as e:
        st.error(f"🚨 Error: {e}")
else:
    st.info("Please upload an image to get a prediction.")

