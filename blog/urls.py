from .views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('category/<int:category_id>/', category, name='category'),
]
