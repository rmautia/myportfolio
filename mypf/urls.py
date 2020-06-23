from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), 
    path('portfolio', views.portfolio, name='portfolio'), 
    path('contact', views.contact, name='contact'), 
]