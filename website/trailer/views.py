# myapp/views.py
from django.shortcuts import render

def trailer_view(request):
    return render(request, 'home1.html')
