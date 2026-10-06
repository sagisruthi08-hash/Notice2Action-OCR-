import streamlit as st
from PIL import Image
from dotenv import load_dotenv

from ocr import extract_text
from llm import analyze_notice

load_dotenv()

st.set_page_config(
    page_title="Notice2Action AI",
    page_icon="📢"
)

st.title("📢 Notice2Action AI")

st.write(
    "Upload a notice and convert it into clear, actionable information."
)

file = st.file_uploader(
    "📤 Upload Notice",
    type=["png", "jpg", "jpeg"]
)

if file:

    image = Image.open(file)

    st.image(
        image,
        caption="Uploaded Notice",
        use_container_width=True
    )

    if st.button("🔍 Analyze Notice"):

        with st.spinner("🔎 Extracting text using OCR..."):

            text = extract_text(image)

        if not text.strip():

            st.error("❌ No text could be detected in the notice.")

        else:

            st.subheader("📝 Extracted Text")

            st.text_area(
                "OCR Result",
                text,
                height=200
            )

            with st.spinner("🤖 Analyzing notice with AI..."):

                result = analyze_notice(text)

            st.subheader("✨ Notice2Action Result")

            st.write(result)

else:

    st.info("👆 Upload a notice image to get started.")