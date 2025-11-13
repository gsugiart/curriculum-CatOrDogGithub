import streamlit as st
from fastai.vision.all import *

st.title("Cat or Dog Classifier")
st.text("Hello this is Gamas")


def extract_breed_name(file_path):
    file_name_parts = file_path.split("/")
    file_path_parts = file_name_parts[len(file_name_parts) - 1].split(".")
    # print(file_path_parts)
    file_path_parts = file_path_parts[0].split("_")
    # print(file_path_parts)
    breed_name = ""
    for i in range(len(file_path_parts)):
        if i != len(file_path_parts) - 1:
            breed_name += file_path_parts[i] + "_"
    # print(file_path_parts)

    if breed_name[0].isupper():
        breed_name = "CAT - " + breed_name
    else:
        breed_name = "DOG - " + breed_name

    breed_name = breed_name[:-1]
    # removes last letter from the name
    return breed_name

pet_breed_model = load_learner("pet_breed_model.pkl")

# file = input("Enter your filename: ")
uploaded_file = st.file_uploader("Choose as image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    fastai_img = PILImage.create(uploaded_file)
    prediction = pet_breed_model.predict(fastai_img)

    img_label = prediction[0]
    st.text(img_label)
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

