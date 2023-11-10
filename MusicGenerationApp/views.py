from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'MusicGenerationApp/index.html')

def predict(request):
    return HttpResponse("<h1>Result</h1>")
