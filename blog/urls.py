from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/', views.post_details, name='post_details'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]
