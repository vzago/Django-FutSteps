from django.urls import path
from trainer import views

#Name Space

app_name = 'trainer'

urlpatterns = [
    path('', views.home, name='home'),
]