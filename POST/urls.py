from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('chats/', views.chats, name='chats'),
    

  
]