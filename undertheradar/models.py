from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(
        verbose_name="email address",
        unique=True,
    )
    username = models.CharField(max_length=40,unique=True)

        
class Posts(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def _str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class CommentSection(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE) # FINISH
    comments = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comments
    
    def get_absolute_url(self):
        return reverse("post_list")
