from django.urls import path
from . import views


urlpatterns = [
    path('', views.n, name='tablica'),
    path('create', views.create, name='create')
]
