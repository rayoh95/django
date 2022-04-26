from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="image")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'like_users')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   #, related_name='comments'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    message = models.TextField()

# posts.Post.author: (fields.E304) Reverse accessor for 'Post.author' clashes with reverse accessor for 'Post.likes'.
#         HINT: Add or change a related_name argument to the definition for 'Post.author' or 'Post.likes'.
# posts.Post.likes: (fields.E304) Reverse accessor for 'Post.likes' clashes with reverse accessor for 'Post.author'.
#         HINT: Add or change a related_name argument to the definition for 'Post.likes' or 'Post.author'.