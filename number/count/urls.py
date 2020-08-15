from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='count-home'),
    path('count/', views.num, name='count'),
    path('about/', views.about, name='about'),
    path('count/counting/', views.counting, name='counting'),
    #path('add_user/', views.add_user, name='add_user'),
    #path('add_user_submit/', views.add_user_submit, name='add_user_submit'),
    
    
    ]