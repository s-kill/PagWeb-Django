from django.shortcuts import render
from .models import Deportista

def index(request):
    queryset = Deportista.objects.all()
    return render(request, 'index.html',{"deportistas":queryset})
