from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view
from PIL import Image
import numpy as np
from .models import predict_image


@api_view(['POST'])
def predict(request):
    """ predict view """
    file = request.FILES.get('file')
    if file:
        try:
            data = Image.open(file)
            img = np.array(data)
            img = np.expand_dims(img, 0)
            class_name, confidence = predict_image(img)
            return JsonResponse({
                'Disease detected': class_name,
                'Confidence': confidence
            })
        except FileNotFoundError:
            return HttpResponseBadRequest("File not found")
        except Exception as e:
            print(f"Error processing image: {e}")
            return HttpResponseBadRequest("Error processing image")
    return HttpResponseBadRequest("Upload an image!")
