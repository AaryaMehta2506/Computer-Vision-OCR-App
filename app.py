import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set this path if you're on Windows (adjust if installed elsewhere)
# Make sure this matches the actual path on your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Streamlit page setup
st.set_page_config(page_title="Image to Text - OCR App", layout="centered")

st.title("Image to Text - OCR App")
st.write("Upload an image, and this app will extract any visible text using Tesseract OCR.")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is None:
    st.info("Please upload an image to start OCR processing.")
else:
    try:
        # Load and show image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert to OpenCV format
        img_array = np.array(image)
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

        st.write("Processing image...")

        # Apply threshold for better OCR results
        processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Perform OCR
        extracted_text = pytesseract.image_to_string(processed)

        # Display extracted text
        st.subheader("Extracted Text")
        st.text_area("Output", extracted_text, height=200)

        # Download button
        st.download_button(
            label="Download Extracted Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
