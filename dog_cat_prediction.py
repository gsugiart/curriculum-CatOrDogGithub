import streamlit as st
from fastai.vision.all import *

st.title("Cat or Dog Classifier")
st.text("Hello this is Gamas")

def is_cat(f):
    return f[0].isupper()

cat_vs_dog_model = load_learner("cat_vs_dog_model.pkl")

# file = input("Enter your filename: ")
uploaded_file = st.file_uploader("Choose as image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    fastai_img = PILImage.create(uploaded_file)
    prediction = cat_vs_dog_model.predict(fastai_img)

    img_label = None

    if prediction[0] == 'True':
        confidence_level = prediction[2][1]
        if confidence_level >= 0.90:
            img_label = f"I am very confident that this is a CAT - {confidence_level:.2%}"
        else:
            img_label = f"I think this is a CAT but not sure - {confidence_level:.2%}"
    else:
        confidence_level = prediction[2][0]
        if confidence_level >= 0.90:
            img_label = f"I am very confident that this is a DOG - {confidence_level:.2%}"
        else:
            img_label = f"I think this is a DOG but not sure - {confidence_level:.2%}"
    st.text(img_label)
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

