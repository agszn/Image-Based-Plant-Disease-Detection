from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import cv2
import numpy as np
import tensorflow as tf

import pandas as pd

from myapp.forms import *
from myapp.models import *

from .models import *

MODEL_PATH = r'model/plant_diease/plant_disase.pickle'
model = pd.read_pickle(MODEL_PATH)


def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        # Handle uploaded image
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_file_url = fs.url(filename)

        # Load the TensorFlow model
        model = tf.keras.models.load_model(MODEL_PATH)

        # Load the test image
        test_img = cv2.imread('.' + uploaded_file_url)  # Adjust the path as necessary
        if test_img is not None:
            # Resize the image to match the model's input shape
            test_img = cv2.resize(test_img, (150, 150))  # Adjust size according to your model
            test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)  # Convert to RGB
            test_img = np.expand_dims(test_img, axis=0)  # Add batch dimension

            # Make predictions on the test image
            prediction = model.predict(test_img)
            predicted_class = np.argmax(prediction)

            return render(request, 'resultplant.html', {'predicted_class': predicted_class})
    return render(request, 'upload_i.html')


def predict(request):
     return render(request,'plantpredict.html')