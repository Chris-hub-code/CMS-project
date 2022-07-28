from unicodedata import name
from django.urls import path
from .import views
from django.urls import re_path as url


urlpatterns = [
    path('signup/', views.signin , name='signnup'),
    path('logggin/', views.login_page , name='logggin'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('complaint/', views.complaints , name='complaint'),
    path('logout/', views.logoutpage , name='logout'),
    path('response/', views.response , name='response'),
    path('profile/', views.profilee , name='profile')
    
    
    
    
    
  
  

]
