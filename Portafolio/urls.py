from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index, formularioUno, formularioDos


urlpatterns = [
    path('index', index),
    path('formOne', formularioUno)
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
