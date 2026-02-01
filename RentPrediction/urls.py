# Create URLs
from django.urls import path
from .views import rentprediction_home, predict_rent

urlpatterns = [
    path('', rentprediction_home),
    path('rent/', predict_rent),
]