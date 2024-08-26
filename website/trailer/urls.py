# myapp/urls.py
from django.urls import path
from .views import trailer_view

urlpatterns = [
    path('', trailer_view, name='trailer'),  # Путь будет /trailer
]
