# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trailer/', include('trailer.urls')),  # Подключение маршрутов приложения по пути /trailer/
    path('about/', include('me.urls')),
    path('anime/', include('anime.urls')),
    path('', include('films.urls')),  # Убедитесь, что путь для films настроен правильно

]
