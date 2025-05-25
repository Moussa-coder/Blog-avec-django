from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='frontpage'),
    path('post/new/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]