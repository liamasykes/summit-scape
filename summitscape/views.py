from django.shortcuts import render
from django.http import HttpResponse
from .models import Mountain

def index(request):
    return render(request, 'index.html')

def mountain_list(request):
    mountains = Mountain.objects.all()
    return render(request, 'mountain_list.html', {'mountains': mountains})