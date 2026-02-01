# Create URLs
from django.urls import path
from .views import qitsol_home, inner_product_view

urlpatterns = [
    path('', qitsol_home, name='qitsol_home'),
    #path('inner-product/', inner_product_view, name='inner_product'),
    path('inner_product/', inner_product_view),
]

