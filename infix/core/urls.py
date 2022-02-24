from .views import *
from django.urls import path

urlpatterns = [
    path('', homepage, name='homepage'),
    path('calculate', calculate, name='calc')
]
