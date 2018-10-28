from .views import *
from django.urls import path

app_name = 'services'

urlpatterns = [
        path('', services, name='services'),
]

