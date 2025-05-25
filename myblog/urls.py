from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='frontpage'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]