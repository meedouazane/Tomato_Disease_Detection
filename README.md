sudo docker run -it -v {PATH}/saved_model/:/saved_model -p 8601:8601 --entrypoint /bin/bash tensorflow/serving
tensorflow_model_server --rest_api_port=8601 --model_name=TDD --model_base_path=/saved_model/tomato/
