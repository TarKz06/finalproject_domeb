from django.urls import path
from .views import PostListView
from .views import PostDetailView
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
