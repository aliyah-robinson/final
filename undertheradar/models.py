from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    age_limit = 13
    age = models.PositiveIntegerField(null=True, blank=True)
    if not age_limit:
        raise ValueError("You must be at least 13 year(s) old in order to create an account.")
        
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
    

#class CommentSection(models.Model):
#    post = models.ForeignKey() # FINISH
#    comments = models.CharField(max_length=140)
#    author = models.ForeignKey(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#    )

#    def __str__(self):
#        return self.comments
#    
#    def get_absolute_url(self):
#        return reverse()""" # FINISH