import streamlit as st
from PIL import Image
import numpy as np
import cv2
from ultralytics import YOLO
import tempfile
import os

model = YOLO("yolov8n.pt")

st.title("Phát hiện đối tượng bằng YOLOv8")

uploaded_file = st.file_uploader("📤 Chọn ảnh", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")


    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        img_path = tmp_file.name
        image.save(img_path)

    results = model(img_path)

    result_img_bgr = results[0].plot()

    result_img_rgb = cv2.cvtColor(result_img_bgr, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Ảnh gốc", use_container_width=True)

    with col2:
        st.image(result_img_rgb, caption="Ảnh sau khi nhận diện", use_container_width=True)

    os.remove(img_path)
    st.success("Phát hiện đối tượng thành công!")