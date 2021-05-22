from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('', views.home, name='rec-home'),
    path('results', views.index, name='index'),
]
