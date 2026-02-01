# Create URLs
from django.urls import path
from .views import substring_view, leet_home

urlpatterns = [
    path('', leet_home),
    path('substring/', substring_view),
]