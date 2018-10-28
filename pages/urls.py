from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', page, name='page'),
]

