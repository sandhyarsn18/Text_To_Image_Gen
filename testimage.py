import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}
st.title("Text to Image Generation")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
prompt=st.text_input("Enter your input")
bt=st.button("Generate Image")
if bt:
    image_bytes = query({
        "inputs": prompt,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    Image = Image.open(io.BytesIO(image_bytes))
    st.image(Image)