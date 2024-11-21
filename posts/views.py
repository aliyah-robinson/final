from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.urls import reverse_lazy
from .models import Post

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "detail_post.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "body",
    )
    template_name = "edit_post.html"


class PostDeleteView(DeleteView): 
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("post_list")

class PostCreateView(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = (
        "title",
        "body",
        "author",
    )