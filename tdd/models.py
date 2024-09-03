#import tensorflow as tf
import numpy as np
import requests

#model = tf.keras.models.load_model('../ML/DL/TL/tomato.keras')
class_names = ['Tomato___Bacterial_spot',
               'Tomato___Early_blight',
               'Tomato___Late_blight',
               'Tomato___Leaf_Mold',
               'Tomato___Septoria_leaf_spot',
               'Tomato___Spider_mites Two-spotted_spider_mite',
               'Tomato___Target_Spot',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
               'Tomato___Tomato_mosaic_virus',
               'Tomato___healthy']


def predict_image(image):
    """" use loaded tf model to detect disease type """
    endpoint = "http://localhost:8601/v1/models/TDD:predict"
    data = {
        "instances": image.tolist()
    }
    try:
        response = requests.post(endpoint, json=data)
        predict = response.json()
        #prediction = model.predict(image)
    except Exception as e:
        print(f"Error predicting image: {e}")
    predicted_class = np.argmax(predict['predictions'])
    confidence = round(np.max(predict['predictions']) * 100, 1)
    confidence = f"{confidence}%"
    class_name = class_names[predicted_class]
    return class_name, confidence
