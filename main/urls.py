from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexs, name='home'),
    path('about', views.about, name='about')
]
