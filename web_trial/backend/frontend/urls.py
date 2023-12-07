from . import views
from django.urls import path 

urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('properties.html', views.property, name='properties.html'),
    path('property-details.html', views.details, name='property-details.html')
]
