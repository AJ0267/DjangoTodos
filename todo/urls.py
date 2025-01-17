from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('mytodos/', views.display_todos, name='mytodos'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('toggle-status/<int:id>/', views.toggle_status, name='toggle_status'),
]
