from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("detail_post")