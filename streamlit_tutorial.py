import streamlit as st

st.title("Cat or Dog Classifier")
st.text("Hello this is Gamas")

file = input("Enter your filename: ")
uploaded_file = st.file_uploader("Choose as image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
