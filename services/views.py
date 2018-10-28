from django.shortcuts import render
from .models import Service

# Create your views here.


def services(request):
    all_services = Service.objects.all()
    return render(request, 'services/services.html', {'services': all_services})
