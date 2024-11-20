from django.views.generic import PostView

from .models import Post

# Create your views here.
class PostListView(PostView):
    model = Post
    template_name = "post_list.html"