from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.destination_list, name='destination-list'),
    # Add more URL patterns for your other views here
]
