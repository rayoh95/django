from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    views = models.IntegerField(default = 0)
    image = models.ImageField(null=True, blank=True, upload_to="image")

class Comment(models.Model):

    # board = models.ForeignKey(Board)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)   #, related_name='comments'
    # author = models.CharField(max_length = 10)
    message = models.TextField()

