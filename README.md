
# Introduction
Welcome to Tomato Disease Detection, deep learning-based model designed to accurately identify and classify various tomato diseases from images of infected leaves. Leveraging advanced techniques like convolutional neural networks (CNNs), the model aims to assist farmers in early disease detection and prevention, leading to increased crop yields and reduced losses.

## Installation
* Clone this repository: `git clone "https://github.com/meedouazane/Tomato_Disease_Detection"`
* Access TrueDetective directory: `cd Tomato_Disease_Detection`
* Run pip to install dependence : `pip3 install -r requirements.txt`
  * Use TensorFlow Serving with Docker to serve savedModel:<br/>
      Once you have Docker installed, you can pull the latest TensorFlow Serving docker image by running:<br/>
          `docker pull tensorflow/serving`<br/>
          `sudo docker run -it -v {PATH}/saved_model/:/saved_model -p 8601:8601 --entrypoint /bin/bash tensorflow/serving`<br/>
          `tensorflow_model_server --rest_api_port=8601 --model_name=TDD --model_base_path=/saved_model/tomato/`<br/>
* Verify if TensorFlow Serving working: http://localhost:8601/v1/models/TDD<br/>
* Run app.py: `python manage.py runserver`<br/>
![Postman](https://i.ibb.co/88f4f38/tomato.jpg)





