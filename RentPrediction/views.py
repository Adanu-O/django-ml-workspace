from django.shortcuts import render


# Creat""e your views here. - new change
from django.http import HttpResponse

def rentprediction_home(request):
     return HttpResponse("""
        <h1>Rent Prediction</h1>
        <ul>
            <li><a href="/leetcode/rent/">Rent Prediction Kolkata</a></li>
        </ul>
        <br>
        <a href="/">⬅ Back to Main Page</a>
    """)


import pickle
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
import os

MODEL_PATH = os.path.join(settings.BASE_DIR, "rentprediction/model/kolkata_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_rent(request):
    try:
        data = {
            'SELLER TYPE': request.GET.get('seller'),
            'BEDROOM': int(request.GET.get('bedroom')),
            'LAYOUT TYPE': request.GET.get('layout'),
            'PROPERTY TYPE': request.GET.get('property'),
            'LOCALITY': request.GET.get('locality'),
            'AREA': request.GET.get('area'),
            'FURNISH TYPE': request.GET.get('furnish'),
            'BATHROOM': int(request.GET.get('bathroom')),
        }

        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]

        return JsonResponse({
            "predicted_rent": round(float(prediction), 2),
            "input": data
        })

    except Exception as e:
        return JsonResponse({"": str(e)}, status=400)

