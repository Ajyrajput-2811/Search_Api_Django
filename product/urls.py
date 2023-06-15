from django.urls import path
from .views  import *

urlpatterns = [
    path('api/', get_product,name = 'product_search')
]