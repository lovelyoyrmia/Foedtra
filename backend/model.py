import json
import os
import tensorflow as tf
import requests
import numpy as np
from PIL import Image
from keras_preprocessing import image
from keras.models import load_model


class Model:
    def __init__(self, base_model=os.path.join(os.getcwd(), 'model', 'foedtra_model3_improve.h5')):
        self.base_model = base_model

    def _loadModel(self):
        return load_model(self.base_model)

    def _normalizeImage(self, img):
        img = tf.keras.preprocessing.image.smart_resize(img, (224, 224))
        img = image.img_to_array(img)
        img = tf.reshape(img, (-1, 224, 224, 3))

        return img

    def _load_json(self):
        dataset = json.load(open('dataframe-traditional-food.json', 'r'))
        for data in dataset['data']:
            data['keyword'] = data['namaMakanan'].lower().replace(' ', '_')
    
        return dataset

    def predict(self, base_image):
        model = self._loadModel()
        dataset = self._load_json()

        # Read the image via file.stream
        image_url = requests.get(base_image, stream=True)
        img = Image.open(image_url.raw)
        img = self._normalizeImage(img)
        predictions = model.predict(img/255)
        predictions = np.argmax(predictions)  
        prediction = dataset['data'][predictions]
        prediction['img'] = base_image

        return prediction
    

