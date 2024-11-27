from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
)

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), 
         name="detail_post"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), 
         name="edit_post"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), 
         name="delete_post"),
    path("new_post/", PostCreateView.as_view(), 
         name="new_post"),
    path("", PostListView.as_view(), 
         name="post_list"),
]