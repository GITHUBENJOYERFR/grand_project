from django.urls import path
from .views import anime

urlpatterns = [
    path('', anime, name='anime'),  # Путь будет /trailer
]