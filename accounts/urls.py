from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginuser, name='loginuser'), 
    path('logout/', views.user_logout, name='logout'), 
]
