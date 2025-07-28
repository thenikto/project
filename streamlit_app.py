import streamlit as st
import requests
from PIL import Image

st.title(" Image Classifier (ResNet50)")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    #st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    image = Image.open(uploaded_file)
    st.image(image, caption="Загруженное изображение", use_column_width=True)


    if st.button("Predict"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://fastapi:8000/predict/", files=files)

        if response.status_code == 200:
            label = response.json()["label"]
            st.success(f"Prediction: {label}")
        else:
            st.error("Prediction failed")