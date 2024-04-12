
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import keras as keras 
import matplotlib.pyplot as plt
import base64


img=Image.open("360_F_524073051_Vy9uJptKxsZslEFXqj3WMQxAcWA3yK6X.jpg")
st.set_page_config(page_title="Potato leaf disease detection",page_icon=img)

background_image_path="istockphoto-809874306-612x612.jpg"
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(background_image_path)

container_style = """
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 20px;
    text-align: center;
    box-shadow: 5 2px 4px rgba(0,0,0,0.1);
    background-color: #dde8d1;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
"""


st.markdown(f'<div style="{container_style}"><h1>Potato Leaf Disease Detection</h1> ',unsafe_allow_html=True)

st.markdown('</div>',unsafe_allow_html=True)
st.divider()

def main() :
    file_uploaded = st.file_uploader('**_choose image of potato leaf_**', type = 'jpg')
    st.divider()
    if file_uploaded is not None :
        image = Image.open(file_uploaded)
        st.subheader("Uploaded Image:")
        figure = plt.figure()
        plt.imshow(image)
        plt.axis('off')
        st.pyplot(figure)
        result, confidence = predict_class(image)
        if result == "Potato__healthy":
            st.success("HEALTHY!",icon="✅")
            st.divider()
            st.subheader("Your potato plant is very :green[**HEALTHY**].")
        elif "Early_blight" in result:
            st.error("INFECTED!",icon="🚨")
            st.divider()
            st.subheader("Sorry to say, your potato plant is infected with :red[**EARLY_BLIGHT**] disease.")
        elif "Late_blight" in result:
            st.error("INFECTED!",icon="🚨")
            st.divider()
            st.subheader("Sorry to say, your potato plant is infected with :red[**LATE_BLIGHT** ]disease.")
 
        st.divider()

        info=st.checkbox('More Info')
        if info:
            st.write('**Prediction** : {}'.format(result))
            st.write('**Confidence** : {}%'.format(confidence))

def predict_class(image):

    # Create the model
    model=tf.keras.models.load_model("my_model.h5")

    # Preprocess the image
    test_image = image.resize((256, 256))
    test_image = keras.preprocessing.image.img_to_array(test_image)
    test_image /= 255.0
    test_image = np.expand_dims(test_image, axis=0)

    # Class names
    class_names = ['Potato__Early_blight', 'Potato__Late_blight', 'Potato__healthy']

    # Make prediction
    prediction = model.predict(test_image)
    confidence = round(100 * np.max(prediction[0]), 2)
    final_pred = class_names[np.argmax(prediction)]

    return final_pred, confidence


if __name__ == "__main__":
    main()

# st.markdown('</div>',unsafe_allow_html=True)
