from . import views
from django.urls import path
urlpatterns = [
    path('', views.startPage, name='home Page')
]