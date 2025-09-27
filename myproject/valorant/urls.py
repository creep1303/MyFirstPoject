from django.urls import path
from .import views
urlpatterns = [path('create_agent/', views.create_agent, name='create_agent'),
               path('create_player/', views.create_player, name='create_player'),
               path('update_agent/<int:b_id>/', views.update_agent, name='update_agent'),
               path('update_player/<int:b_id>/', views.update_player, name='update_player'),
               path('delete_player/<int:b_id>/', views.delete_player, name='delete_player'),
               path('delete_agent/<int:b_id>/', views.delete_agent, name='delete_agent'),]
