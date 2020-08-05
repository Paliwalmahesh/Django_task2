from django.urls import path
from . import views

urlpatterns = [
    path('', views.num, name='count'),
    path('about/', views.about, name='about'),
    path('counting', views.counting, name='about'),
    
    ]