import io
import streamlit as st
from PIL import Image


import numpy as np
import cv2

import pathlib
import os


def PreprocessAndPredict(image):
    # Define list of class names
    # class_names = ["Acne", "Eczema", "Atopic", "Psoriasis", "Tinea", "Vitiligo"]
    #
    # # Load saved model
    # model = keras.models.load_model("C:\\Users\\User\\Downloads\\6claass.h5")
    # vgg_model = VGG19(weights='imagenet', include_top=False, input_shape=(180, 180, 3))

    # Load and preprocess image
    img = cv2.imread(image)
    img = cv2.resize(img, (180, 180))
    # img = np.array(img) / 255.0
    # img = np.expand_dims(img, axis=0)
    # img = vgg_model.predict(img)
    # img = img.reshape(1, -1)

    # Make prediction on preprocessed image
    # pred = model.predict(img)[0]
    # predicted_class_index = np.argmax(pred)
    # predicted_class_name = class_names[predicted_class_index]

    # return predicted_class_name
    return img
def load_image():
    """Создание формы для загрузки изображения"""
    # Форма для загрузки изображения
    uploaded_file = st.file_uploader(
        label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        # Получение загруженного изображения
        image_data = uploaded_file.getvalue()
        # Показ загруженного изображения на Web-странице
        st.image(image_data)
        image = Image.open(uploaded_file)
        image = image.save("img.jpg")

        # Возврат изображения в формате PIL
        return image
    else:
        return None


# Выводим заголовок страницы
st.title('Классификатор кожных заболеваний')
# Вызываем функцию создания формы загрузки изображения
img = load_image()
st.write(img)



img2 = (os.path.abspath(path=str(img)))
st.write(img2)
# Добавим кнопку-команду
result = st.button("Распознать изображение")

if result:
    st.write('**Результат распознования:**')
    st.image(PreprocessAndPredict("img.jpg"))
