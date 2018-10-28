from .views import *
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('store/', store, name='store'),

]

